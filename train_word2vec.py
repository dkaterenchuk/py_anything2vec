#! /usr/bin/env python

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


Given a set of cleaned/parsed text, this script trains a new word2vec model.
The text data must be prepared by the user. It usually contains one sentence per
line and each sentence consists of lower case words separated by space without any
punctuation.

Usage:
    python train_word2vec.py <doc_path.txt> <output_path.model> [n_number_of_dimensions]

Args:
    doc_path.txt - a path to a document in txt format that will be used to train word2vec
    output_path.model - a path to save trained model
    n_number_of_dimentions - [optional] integer number to define the number of dimensions

Example:
    $ python train_word2vec.py test_data/test.txt test_data/test.model 2

or:
    $ python train_word2vec.py test_data/test.txt test_data/test.model
"""

import sys
from gensim.models.doc2vec import Word2Vec


def read_file(doc_path):
    """
    Reads a file and returns a list of sentences (list of words)

    Args:
        doc_path - str: path to a file

    Returns:
        sentences - list[[],[],..]: list of lists of words
    """
    sentences = []
    with open(doc_path, "r") as f:
        for line in f:
            sentences.append(line.encode('utf-8').strip("\n").split(" "))
            
    return sentences


def train_model(doc_path, output_path, dim=100):
    """
    Training a model.
    Reading the file, building a vocabulary, training, and saving the model

    Args:
        doc_path - str: path to a doc file
        output_path - str: path to the model
    """
    print "Reading a file ..."
    sentences = read_file(doc_path)
    print "Training a model ..."
    model = Word2Vec(sentences, min_count=0, size=dim, window=10)
    print "Saving the moles ..."
    model.save(output_path)
    print "Done."
    

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
            main(sys.argv[1], sys.argv[2], int(sys.argv[3]))
