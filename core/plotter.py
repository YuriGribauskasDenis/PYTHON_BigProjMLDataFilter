from matplotlib import pyplot as plt
import seaborn as sns
import numpy as np
from .reporter import Reporter

class Plotter(Reporter):

    def plot_all(self):
        self.__plot_big()
        self.__plot_matrix()

    def __plot_big(self):
        dims = 12, 7
        dep = 72

        plt.clf()

        _, ax = plt.subplots(1, 1, figsize = dims, dpi = dep)
        ax.plot(self.tester.history.history['accuracy'])
        ax.plot(self.tester.history.history['val_accuracy'])
        ax.set_title('model accuracy')
        ax.set_ylabel('accuracy')
        ax.set_xlabel('epoch')
        ax.legend(['train', 'val'], loc='upper left')
        adr = f'{self.save_to_fldr}/accuracy_{self.tester.i:03d}.png'
        plt.savefig(adr)

        _, ax = plt.subplots(1, 1, figsize = dims, dpi = dep)
        ax.plot(self.tester.history.history['loss'])
        ax.plot(self.tester.history.history['val_loss'])
        ax.set_title('model loss')
        ax.set_ylabel('loss')
        ax.set_xlabel('epoch')
        ax.legend(['train', 'val'], loc='upper left')
        adr = f'{self.save_to_fldr}/loss_{self.tester.i:03d}.png'
        plt.savefig(adr)


    def __plot_matrix(self):
        plt.clf()
        group_counts = [f'{value:d}' for value in self.tester.cf_matrix.flatten()]
        group_percentages = [f'{value*100:.2f}%' for value in self.tester.cf_matrix.flatten()/np.sum(self.tester.cf_matrix)]
        labels = [f'{v1}\n{v2}' for v1, v2 in
                zip(group_counts,group_percentages)]
        labels = np.asarray(labels).reshape(2,2)
        sns.heatmap(self.tester.cf_matrix, annot=labels, fmt='', cmap='Blues')
        adr = f'{self.save_to_fldr}/hist_{self.tester.i:03d}.png'
        plt.savefig(adr)