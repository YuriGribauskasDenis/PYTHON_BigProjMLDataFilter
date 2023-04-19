from tensorflow.keras.models import Model, Sequential
from tensorflow.keras.layers import Input, Concatenate
from tensorflow.keras.layers import Dense, Conv2D, DepthwiseConv2D, Dropout, Flatten
from tensorflow.keras.layers import GlobalAveragePooling2D, Reshape
from tensorflow.keras.layers import MaxPooling2D, AveragePooling2D
from tensorflow.keras.layers import ReLU, Softmax, LeakyReLU
from tensorflow.keras.layers import BatchNormalization as BN
from tensorflow.keras import regularizers


def gen_network():
    netw = small_network()
    return netw

def small_network():

    first = Input((100,100,1))
    model = MaxPooling2D(pool_size=2) (first)

    # lambd = 0.1
    reglar = regularizers.L1L2(l1=1e-5, l2=1e-4)

    model = Conv2D (16, kernel_size=3, strides=1, padding='same', kernel_regularizer=reglar) (model)
    model = ReLU() (model)
    model = Conv2D (16, kernel_size=3, strides=1, padding='same', kernel_regularizer=reglar) (model)
    model = ReLU() (model)
    model = AveragePooling2D(pool_size=(2, 2)) (model)

    model = Conv2D (24, kernel_size=3, strides=1, padding='same', kernel_regularizer=reglar) (model)
    model = ReLU() (model)
    model = Conv2D (24, kernel_size=3, strides=1, padding='same', kernel_regularizer=reglar) (model)
    model = ReLU() (model)
    model = AveragePooling2D(pool_size=(2, 2)) (model)

    model = Conv2D (32, kernel_size=3, strides=1, padding='same', kernel_regularizer=reglar) (model)
    model = ReLU() (model)
    model = Conv2D (32, kernel_size=3, strides=1, padding='same', kernel_regularizer=reglar) (model)
    model = ReLU() (model)
    model = AveragePooling2D(pool_size=(2, 2)) (model)

    model = Conv2D (48, kernel_size=3, strides=1, padding='same', kernel_regularizer=reglar) (model)
    model = GlobalAveragePooling2D() (model)
    model = Flatten() (model)
    model = Dense(2) (model)
    last = Softmax() (model)
    final = Model(first, last)

    return final