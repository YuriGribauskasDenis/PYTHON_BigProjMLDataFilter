from core import ModelHandler, DataRaiser

dr = DataRaiser()
X_inp, Y_inp, I_inp, _ = dr.dater()

mh = ModelHandler()
mh.complex_train(X_inp, Y_inp, I_inp)

print('ALL DONE')