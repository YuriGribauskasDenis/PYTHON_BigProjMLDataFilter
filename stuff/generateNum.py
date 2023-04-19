import numpy as np

def unison_shuffle4(a,b,c):
    assert len(a) == len(b) == len(c)
    p = np.random.permutation(len(a))
    return a[p], b[p], c[p]

def standartize(img):
    return (img - np.mean(img)) / np.std(img)