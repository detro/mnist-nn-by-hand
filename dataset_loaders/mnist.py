"""Dataset loader for MNIST

This returns the MNIST dataset, numpy-formatted.
"""

from mnist import MNIST

mndata = MNIST('datasets/MNIST', mode='vanilla', return_type='numpy', gz=True)

def load_training():
    return mndata.load_training()

def load_testing():
    return mndata.load_testing()

def display():
    mndata.display(0)