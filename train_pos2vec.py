#!/usr/bin/env python

"""
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

    def __init__(self, reddit_path):
        self.path = reddit_path

    def __iter__(self):
        """
        Reads Reddit json archive (30GB) line by line
        and calls parser on each comment.
        :param reddit_path:
        :return:
        """
        uid = 0
        with open(self.path, "r") as f:
            for line in f:
                uid += 1
                yield TaggedDocument(words=line.strip("\n").split(" "), tags=uid)


def read_data(data_path):
    """
    This function should be used on smalled datasents that can fit into memory, otherwise, use DataReader object.

    :param data_path: path to text data
    :return:
    """
    sentences = []
    with open(data_path, "r") as f:
        for line in f:
            sentences.append(line.strip("\n").split(" "))

    return sentences


def train_model(vocab_path, data_path, trained_path, dim=10):
    model = Doc2Vec(size=dim, workers=8)
#    vocab = DataReader(vocab_path)
#    sentences = DataReader(data_path)
    model.build_vocab(DataReader(data_path))
    # gensim.models.Doc2Vec(sentences, size=dim, workers=8)  #.Word2Vec(sentences, size=dim, workers=8)
    model.train(DataReader(data_path))
    model.save(trained_path+"/test2vec_"+str(dim)+".model")


def main(vocab_path, data_path, trained_path):
    train_model(vocab_path, data_path, trained_path, 100)


if __name__ == "__main__":
    if len(sys.argv) != 4:
        print __doc__
    else:
        main(sys.argv[1], sys.argv[2], sys.argv[3])
