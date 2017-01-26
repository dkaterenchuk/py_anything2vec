#!/usr/bin/env python

"""
Train POS2vec encodings for reddit data

Usage:
    $ python train_pos2vec.py <reddit_pos.txt> <trained_model_path>

"""

import sys
from gensim.models.doc2vec import TaggedDocument, Doc2Vec
from reddit_json_data_reader import RedditReader


class RedditReader(object):

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
                yield TaggedDocument(words=line.strip("\n").split(","), tags=uid)

def build_vocab()

def read_data(data_path):
    with open(data_path, "r") as f:
        sentences = [x.split(",") for x in f.read().split(("\n"))]
    return sentences

def read_data(data_path):
    with open(data_path, "r") as f:
        for line in f:
            yield line.strip("\n").split(",")
        #sentences = [x.split(",") for x in f.read().split(("\n"))]
    #return sentences

def train_model(vocab_path, data_path, trained_path, dim=10):
    #print sentences[:3]
    model = Doc2Vec(size=dim, workers=8)
    vocab = RedditReader(vocab_path)
    sentences = RedditReader(data_path)
    model.build_vocab(vocab)
    #gensim.models.Doc2Vec(sentences, size=dim, workers=8)  #.Word2Vec(sentences, size=dim, workers=8)
    model.train(sentences)
    model.save(trained_path+"/test2vec_"+str(dim)+".model")


def main(vocab_path, data_path, trained_path):
    train_model(vocab_path, data_path, trained_path, 100)


if __name__ == "__main__":
    if len(sys.argv) != 4:
        print __doc__
    else:
        main(sys.argv[1], sys.argv[2], sys.argv[3])
