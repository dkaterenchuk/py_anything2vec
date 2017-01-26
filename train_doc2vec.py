#!/usr/bin/env python

"""
#############################################################################
MIT License

Copyright (c) 2017 Denys Katerenchuk

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
#############################################################################


Train a doc2vec model from a given set of cleaned/parsed text. The text data must be prepared by the user.
It usually contains one document per line and each document consists of lower case words separated by space
without any punctuation.

Usage:
    $ python train_pos2vec.py <reddit_pos.txt> <trained_model_path> [n_number_of_dimensions]

Args:
    doc_path.txt - a path to a document in txt format that will be used to train doc2vec
    output_path.model - a path to save trained model
    n_number_of_dimentions - [optional] integer number to define the number of dimensions

Example:
    $ python train_doc2vec.py test_data/test.txt test_data/test.model 2

or:
    $ python train_doc2vec.py test_data/test.txt test_data/test.model
"""

import sys
from gensim.models.doc2vec import TaggedDocument, Doc2Vec


class DataReader(object):

    def __init__(self, doc_path):
        self.path = doc_path

    def __iter__(self):
        """
        Reads a large archive line by line without loading it into ram.
        This approach is limited by the read speed and is designed to work with large files.

        :param reddit_path:
        :return: iterator
        """
        uid = 0
        with open(self.path, "r") as f:
            for line in f:
                uid += 1
                yield TaggedDocument(words=line.strip("\n").split(" "), tags=["sent_"+str(uid)])


def read_data(data_path):
    """
    Reads smaller data that can fit into RAM. It is much faster but should be used on smalled
    datasets, otherwise, use DataReader object.

    :param data_path: path to text data
    :return: sentences: - a list of sentences which are just lists of words
    """
    sentences = []
    with open(data_path, "r") as f:
        for line in f:
            sentences.append(line.strip("\n").split(" "))

    return sentences


def train_model(doc_path, model_path, dim=100):
    """
    Trains Doc2Vec model

    :param doc_path: - str: path to a doc file
    :param model_path: - str: paht to output_model_file
    :param dim: - [optional] - number of dimentions
    :return:
    """
    print "Initializing a model"
    model = Doc2Vec(size=dim, workers=8)

    print "Building vocabulary..."
    model.build_vocab(DataReader(doc_path))
    print "Training the model..."
    model.train(DataReader(doc_path))
    print "Saving the model to %s" % model_path
    model.save(model_path)


def main(doc_path, output_path, dim=100):
    """
    Main function
    """
    train_model(doc_path, output_path, dim)


if __name__ == "__main__":
    if len(sys.argv) != 3 and len(sys.argv) != 4:
        print __doc__
    else:
        if len(sys.argv) == 3:
            main(sys.argv[1], sys.argv[2])
        else:
            main(sys.argv[1], sys.argv[2], sys.argv[3])
