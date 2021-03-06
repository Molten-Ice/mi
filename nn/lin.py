
#################################################
### THIS FILE WAS AUTOGENERATED! DO NOT EDIT! ###
#################################################
# file to edit: docs/nn_lin.ipynb

import sys
from pathlib import Path
sys.path.append(Path.cwd().parent.as_posix())
from nn.neural import Neural
import torch
import math

class Lin(Neural):
    def __init__(self, n_in, n_out):
        self.w = torch.randn(n_in,n_out)*math.sqrt(2./n_in)
        self.b = torch.zeros(n_out)
        self.w.g = None
        self.b.g = None

    def __repr__(self): return "Linear(in_features="+str(self.w.shape[0])+", out_features="+str(self.b.shape[0])+")"

    def parameters(self):
        return self.w, self.b

    def forward(self, inp): return inp@self.w + self.b

    def bwd(self, out, inp):
        print(out.shape)
        print(hasattr(out, 'g'))
        inp.g = out.g @ self.w.t()
        self.w.g = inp.t() @ out.g
        #self.w.g = torch.einsum("bi,bj->ij", inp, out.g)
        self.b.g = out.g.sum(0)