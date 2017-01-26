# py_anything2vec
A set of scripts to train your own word2vec, doc2vec or any other "data" 2vec representation.

### Description
These scripts implement training of word2vec and doc2vec models. Gensim library is used as the
backend. There exists a number of trained word2vec models. You should use these scripts if you
need to train a new model on your own data. Otherwise, I recommend downloading one from here:


### Usage
The usege fro training word2vec or doc2vec is identical. In the example below, substitute the script
name for the intended script.

Given a set of cleaned/parsed text, this script trains a new word2vec model.
The text data must be prepared by the user. It usually contains one sentence per line and each
sentence consists of lower case words separated by space without any punctuation.

Usage:
    `python train_word2vec.py <doc_path.txt> <output_path.model> [n_number_of_dimensions]`

Args:
    doc_path.txt - a path to a document in txt format that will be used to train word2vec
    
    output_path.model - a path to save trained model
    
    n_number_of_dimentions - [optional] integer number to define the number of dimensions

### Running

    `$ python train_word2vec.py test_data/test.txt test_data/test.model 2`

or:

    `$ python train_word2vec.py test_data/test.txt test_data/test.model`


### Installation

Download or clone the package and follow the usage instructions to run it.

### Dependencies
Gensim - a python library to train word2vec (https://radimrehurek.com/gensim/)
`pip install gensim`

SciPy - https://www.scipy.org/
`pip install scipy`

NumPy - http://www.numpy.org/
`pip install numpy`

### License

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
