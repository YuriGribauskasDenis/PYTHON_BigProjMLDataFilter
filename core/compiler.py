from .models import gen_network
import tensorflow.keras.backend as BCKN
from tensorflow.keras.preprocessing.image import ImageDataGenerator
import tensorflow as tf
import numpy as np
from constants import ap_obj
from constants import np_obj
from constants import sp_obj
from tensorflow.keras.callbacks import ReduceLROnPlateau, EarlyStopping, ModelCheckpoint
from stuff.generateNum import standartize, unison_shuffle4
from sklearn.utils import class_weight
from .modelTester import ModelTester

class ModelHandler:
    
    def __init__(self):
        self.__checkpoint_filepath_root = ap_obj.getData('CHECK_POINT_FLDR')
        self.__adr_zero = f'{self.__checkpoint_filepath_root}/weights_zero.h5'
        self.__compiled_model = self.__compiler()
    
    @property
    def compiled_model(self):
        return self.__compiled_model

    def __compiler(self):
        BCKN.clear_session()
        model = gen_network()
        model.summary()

        optimizer = tf.keras.optimizers.SGD(learning_rate=0.01, momentum=0.9, nesterov=False, clipnorm=1.0)
        loss_fn = tf.keras.losses.SparseCategoricalCrossentropy()
        model.compile(loss=loss_fn, optimizer=optimizer, metrics=['accuracy'])

        model.save_weights(self.__adr_zero)

        return model

    def __get_data_augmented(self, x, y, b):
        train_datagen_vals = ImageDataGenerator(
            shear_range=0.2,
            zoom_range=0.2,
            rotation_range=15,
            horizontal_flip=True
            )
        gen = train_datagen_vals.flow(
            x,
            y,
            batch_size=b,
            shuffle=False,
        )
        return gen

    def complex_train(self, X_inp, Y_inp, I_inp):
        resultC0 = np.where(Y_inp == 0)[0]
        resultC1 = np.where(Y_inp == 1)[0]

        batch_size = np_obj.getData('BATCH_SIZE')
        dnd_ratio = np_obj.getData('DND_RATIO')
        tvt_ratio = np_obj.getData('TVT_RATIO')

        epochs = np_obj.getData('EPOCHS')

        cont_train = sp_obj.getData('GEN_CSV')

        perc = tvt_ratio
        ST = len(resultC1) * dnd_ratio
        cuts = len(resultC0) // ST + 1

        reduce_lr = ReduceLROnPlateau(monitor='loss', factor=0.2,
                                    patience=5, min_lr=0)

        early_stop = EarlyStopping(monitor='val_loss', patience=10)

        for i in range(cuts):

            Xpa = np.concatenate((X_inp[resultC0[ST * i : ST * (i + 1)]], X_inp[resultC1]), axis=0)
            Ypa = np.concatenate((Y_inp[resultC0[ST * i : ST * (i + 1)]], Y_inp[resultC1]), axis=0)
            Ipa = np.concatenate((I_inp[resultC0[ST * i : ST * (i + 1)]], I_inp[resultC1]), axis=0)
            I_shuff, X_shuff, Y_shuff = unison_shuffle4(Ipa, Xpa, Ypa)

            X = standartize(X_shuff)
            Y = Y_shuff

            total = len(X)
            split = int(total * perc)

            X_train = X[:-split]
            Y_train = Y[:-split]
            x_test = X[-split:]
            y_test = Y[-split:]

            x_val = X_train[-split:]
            y_val = Y_train[-split:]
            x_train = X_train[:-split]
            y_train = Y_train[:-split]

            train_datagenerator = self.__get_data_augmented(x_train, y_train, batch_size)
            validation_datagenerator = self.__get_data_augmented(x_val, y_val, batch_size)
            #test_datagenerator = self.__get_data_augmented(x_test, y_test, batch_size)

            checkpoint_filepath = f'{self.__checkpoint_filepath_root}/model_best_{i:03d}.h5'

            model_checkpoint_callback = tf.keras.callbacks.ModelCheckpoint(
                filepath=checkpoint_filepath,
                save_weights_only=False,
                #verbose=1,
                monitor='val_loss',
                mode='min',
                save_best_only=True)

            class_weights = class_weight.compute_class_weight(
                                                            class_weight = "balanced",
                                                            classes = np.unique(Y_train),
                                                            y = Y_train   
                                                            )
            class_weights = dict(zip(np.unique(Y_train), class_weights))

            print('*'*88)

            # training
            #======================
            my_epochs = epochs

            if not cont_train:
                self.__compiled_model.load_weights(self.__adr_zero)
                BCKN.set_value(self.__compiled_model.optimizer.learning_rate, 0.01)

            history0 = self.__compiled_model.fit(
                train_datagenerator,
                batch_size=batch_size,
                epochs=my_epochs,
                class_weight=class_weights,
                validation_data=validation_datagenerator,
                callbacks=[reduce_lr, model_checkpoint_callback],
                verbose=1
            )
            # last_path = f'{self.__checkpoint_filepath_root}/model_last_{i:03d}.h5'
            # self.__compiled_model.save(last_path)
            print(history0.history)

            # mini results
            #======================
            mt = ModelTester(history0, checkpoint_filepath, i)
            #mt = ModelTester(history0, last_path, i)
            mt.test(x_test, y_test)

            choose_X = X_inp[resultC0]
            choose_Y = Y_inp[resultC0]
            choose_I = I_inp[resultC0]

            mt.loss_it(choose_X, choose_Y, choose_I)
        
        print('TRAINING DONE')