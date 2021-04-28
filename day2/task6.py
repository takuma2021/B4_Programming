# -*- coding: utf-8 -*-
"""
Created on Fri Apr 23 11:45:58 2021

@author: takum
"""

import numpy as np

class SingleLayer:
    def __init__(self,W,b):
        self.W = W
        self.b = b
        
    def ReLU(self,x):
        self.x = x
        y = np.dot(self.x,self.W) + self.b
        return y

x = np.array([1.0, 0.5])
W = np.array([[0.1, 0.3, 0.5], [0.2, 0.4, 0.6]])
b = np.array([0.1, 0.2, 0.3])

p = SingleLayer(W, b)
print(p.ReLU(x))