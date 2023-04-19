from matplotlib import pyplot as plt

def my_plot_big(history, i):
    dims = 12, 7
    dep = 72

    _, ax = plt.subplots(1, 1, figsize = dims, dpi = dep)
    ax.plot(history.history['accuracy'])
    ax.plot(history.history['val_accuracy'])
    ax.set_title('model accuracy')
    ax.set_ylabel('accuracy')
    ax.set_xlabel('epoch')
    ax.legend(['train', 'val'], loc='upper left')
    # adr = f'{checkpoint_filepath_root}/accuracy_0{i:03d}.png'
    # plt.savefig(adr)

    _, ax = plt.subplots(1, 1, figsize = dims, dpi = dep)
    ax.plot(history.history['loss'])
    ax.plot(history.history['val_loss'])
    ax.set_title('model loss')
    ax.set_ylabel('loss')
    ax.set_xlabel('epoch')
    ax.legend(['train', 'val'], loc='upper left')
    # adr = f'{checkpoint_filepath_root}/loss_0{i:03d}.png'
    # plt.savefig(adr)