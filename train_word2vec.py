#! /usr/bin/env python

"""
Given a set of cleaned/parsed sentences, this script train a new word2vec model.

Usage:
    python train_word2vec.py <doc_path.txt> <output_path.model> 

"""
import sys
from gensim.models.doc2vec import Word2Vec

DIM = 2  # number of dimentions


def read_file(doc_path):
    """
    Reads a file (large) and returns a list of sentences (list of words)

    Args:
        doc_path - str: path to a file

    Returns:
        sentences - list[[]]: list of lists of words
    """
    sentences = []
    with open(doc_path, "r") as f:
        for line in f:
            sentences.append(line.encode('utf-8').strip("\n").split(","))
            
    return sentences


def train_model(doc_path, output_path):
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
    model = Word2Vec(sentences, min_count=0, size=2, window=10)
    print "Saving the moles ..."
    model.save(output_path)
    print "Done."
    

def main(doc_path, output_path):
    """
    Main function
    """
    train_model(doc_path, output_path)


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print __doc__
    else:
        main(sys.argv[1], sys.argv[2])
