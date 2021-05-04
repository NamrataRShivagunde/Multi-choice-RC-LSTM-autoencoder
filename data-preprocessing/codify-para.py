# -*- coding: utf-8 -*-

from __future__ import division, print_function, unicode_literals

import argparse
import numpy as np
import tensorflow as tf
import os

import utils
from autoencoder import TextAutoencoder

import pandas as pd
import nltk
nltk.download('punkt')

"""
Run the encoder part of the autoencoder in a corpus to generate
the memory cell representation for them.
"""

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('model', help='Directory with saved model')
    parser.add_argument('input', help='File with one sentence per line')
    parser.add_argument('vocabulary', help='File with autoencoder vocabulary')
    parser.add_argument('output', help='Numpy file to write output')

    args = parser.parse_args()

    wd = utils.WordDictionary(args.vocabulary)
    sess = tf.InteractiveSession()
    model = TextAutoencoder.load(args.model, sess)

    excelfile = args.input
    para = pd.read_excel(excelfile)
    all_states = []
    for i in range(len(para)):
        sents = nltk.tokenize.sent_tokenize(para['paragraph'][i])
        sentences, sizes = utils.load_text_data_from_list(sents, wd)
        state = model.encode(sess, sentences, sizes)
        state = state.mean(axis=0)
        all_states.append(state)
        print(len(all_states))

    
    state = np.vstack(all_states)
    print("final state", state.shape)
    np.save(args.output, state)
