
#################################################
### THIS FILE WAS AUTOGENERATED! DO NOT EDIT! ###
#################################################
# file to edit: docs/nn_sequentialModel.ipynb

import sys
from pathlib import Path
sys.path.append(Path.cwd().parent.as_posix())
from nn.module import Module

class SequentialModel(Module):
    def __init__(self, layers, loss):
        self.layers = layers
        self.loss = loss