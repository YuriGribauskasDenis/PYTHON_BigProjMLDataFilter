import tensorflow as tf
from constants import np_obj
import numpy as np
from .plotter import Plotter
from .losser import Losser
from stuff.generateNum import standartize
from sklearn.metrics import confusion_matrix

class ModelTester:

    def __init__(self, history, adr, i):
        self.__history = history
        self.__test_model = tf.keras.models.load_model(adr)
        self.__i = i

    @property
    def history(self):
        return self.__history

    @property
    def test_model(self):
        return self.__test_model

    @property
    def i(self):
        return self.__i

    @property
    def cf_matrix(self):
        return self.__cf_matrix
    
    def __plot(self):
        pl = Plotter(self)
        pl.plot_all()

    def test(self, x_test, y_test):
        batch_size = np_obj.getData('BATCH_SIZE')
        x_test = standartize(x_test)

        results = self.__test_model.evaluate(x_test, y_test, batch_size=batch_size)
        print("test loss, test acc:\n", results)

        ju = 15
        print(f"Generate predictions for {ju} samples")
        predicts = self.__test_model.predict(x_test)
        print("predictions shape:\n", predicts.shape)
        print(predicts[:ju])

        # matrix
        #======================
        y_pred = np.argmax(predicts, axis = 1)
        self.__cf_matrix = confusion_matrix(y_test, y_pred)
        print(self.__cf_matrix)

        self.__plot()

    def loss_it(self, choose_X, choose_Y, choose_I):

        lo = Losser(self)
        lo.generate(choose_X, choose_Y, choose_I)
        lo.write()
