import numpy as np
import torch

def add(a,b):
    return a+b

class resnet(torch.nn.Module):
    def __init__(self):
        self.__super__().__init__()
        self.name = 'resnet'

    def forward(self, x):
        return x

