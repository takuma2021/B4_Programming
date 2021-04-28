# -*- coding: utf-8 -*-
"""
Created on Sat Apr 24 20:53:44 2021

@author: takum
"""

import numpy as np

class Affine:
    def __init__(self, W, b):
        self.W =W
        self.b = b
        
        self.x = None
        self.original_x_shape = None
        # 重み・バイアスパラメータの微分
        self.dW = None
        self.db = None

    def forward(self, x):
        self.x = x
        out = np.dot(self.x, self.W) + self.b

        return out

    def backward(self, dout):
        dx = np.dot(dout, self.W.T)
        self.dW = np.dot(self.x.T, dout)
        self.db = np.sum(dout, axis=0)
        
        return dx
    
x = np.array([[1.0, 0.5], [-0.4, 0.1]])
W = np.array([[0.1, 0.3, 0.5], [0.2, 0.4, 0.6]])
b = np.array([0.1, 0.2, 0.3])

n = Affine(W, b)
a = n.forward(x)
print(a)
db = n.backward([1,1],[1,1],[1,1])
print(db)