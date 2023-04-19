from constants import ap_obj, sp_obj
from pathlib import Path
import hashlib
import csv
import numpy as np
import cv2

class DataRaiser:

    def __init__(self):
        self.__folderC0 = ap_obj.getData('NODEFECT_FLDR')
        self.__folderC1 = ap_obj.getData('DEFECT_FLDR')
        self.__fname = ap_obj.getData('DUMP_FILE')
        self.__dataset_adress = ap_obj.getData('ZIP_FILE')

    def __from_fldr(self):
        c0f = list(Path(self.__folderC0).iterdir())
        c1f = list(Path(self.__folderC1).iterdir())
        filelist = [c0f, c1f]
        return filelist

    def __gen_csv(self, filelist):
        with open(self.__fname, 'w') as f:
            count = 0
            for i, group in enumerate(filelist):
                for el in group:
                    name = str(el)
                    # count - index, name - address, i - class, hash - hash
                    f.write(f'{count},{name},{i},')
                    count += 1
                    with open(name, "rb") as fimg:
                        bytes = fimg.read() # read entire file as bytes
                        readable_hash = hashlib.sha256(bytes).hexdigest();
                        f.write(f'{readable_hash}\n')

    def __from_csv(self):
        with open(self.__fname, 'r') as read_f:
            csvreader = csv.reader(read_f)
            rows = [row for row in csvreader]

            idxs, adrs, lbls, hashs = list(zip(*rows))
            X_inp = np.array([np.array(cv2.imread(fname, 0)[...,None]) for fname in adrs])
            Y_inp = np.array(lbls, dtype = np.int8)
            indexes = np.array(idxs, dtype = np.int32)
            hash_codes = np.array(hashs)

            return X_inp, Y_inp, indexes, hash_codes

    def __gen_zip(self, cartridge):
        X_inp, Y_inp, indexes, hash_codes = cartridge
        np.savez(self.__dataset_adress, i=indexes, x=X_inp, y=Y_inp, h=hash_codes)

    def __from_zip(self):
        npzfile = np.load(self.__dataset_adress)

        X_inp = npzfile['x']
        Y_inp = npzfile['y']
        I_inp = npzfile['i']
        H_inp = npzfile['h']

        return X_inp, Y_inp, I_inp,  H_inp

    def dater(self):
        from_fldr = sp_obj.getData('FROM_FLDR')

        if from_fldr:
            filelist = self.__from_fldr()
            self.__gen_csv(filelist)
            cartridge = self.__from_csv()
            self.__gen_zip(cartridge)

        return self.__from_zip()