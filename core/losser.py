from .reporter import Reporter
import tensorflow as tf
import csv

class Losser(Reporter):
    
    def generate(self, choose_X, choose_Y, choose_I):
        loss_fn_test = tf.keras.losses.SparseCategoricalCrossentropy(reduction='none')
        loss_vals = loss_fn_test(choose_Y, self.tester.test_model.predict(choose_X))

        res = {k : float(v) for k, v in zip(choose_I, loss_vals)}
        self.__res_sorted = {k : v for k, v in sorted(res.items(), key = lambda x: x[1], reverse=True)}

    def write(self):
        self.save_to_fldr
        adr = f'{self.save_to_fldr}/res_loss_{self.tester.i:03d}.csv'
        with open(adr, 'w', newline='') as f:
            writer = csv.writer(f)
            for i, (k, v) in enumerate(self.__res_sorted.items()):
                writer.writerow([k,v])