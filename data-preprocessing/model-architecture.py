# -*- coding: utf-8 -*-

from __future__ import division, print_function, unicode_literals

import argparse
import numpy as np
import tensorflow as tf
import os

import utils
from autoencoder import TextAutoencoder


"""
Run the encoder part of the autoencoder in a corpus to generate
the memory cell representation for them.
"""

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('model', help='Directory with saved model')
    
    args = parser.parse_args()
    sess = tf.InteractiveSession()
    model = TextAutoencoder.load(args.model, sess)
    model.summary()

    