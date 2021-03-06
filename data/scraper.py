
#################################################
### THIS FILE WAS AUTOGENERATED! DO NOT EDIT! ###
#################################################
# file to edit: docs/data_scraper.ipynb

from fastai import datasets
import pickle
import gzip
from torch import tensor

urls = {"MNIST_URL" : 'http://deeplearning.net/data/mnist/mnist.pkl'}

def get_data(url = "MNIST_URL"):
    path = datasets.download_data(urls[url], ext='.gz')
    with gzip.open(path, 'rb') as f:
        ((x_train, y_train), (x_valid, y_valid), _) = pickle.load(f, encoding='latin-1')
    return map(tensor, (x_train,y_train,x_valid,y_valid))