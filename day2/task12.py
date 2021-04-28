# -*- coding: utf-8 -*-
"""
Created on Sat Apr 24 20:43:43 2021

@author: takum
"""

import numpy as np

class Sigmoid():
    def __init__(self):
        self.out = None

    def forward(self, x):
        out = 1 / (1 + np.exp(-x))
        self.out = out
        return out

    def backward(self, dout):
        dx = dout * (1.0 - self.out) * self.out

        return dx

x = np.array([-0.5, 0.0, 1.0, 2.0])
n = Sigmoid()
a = n.forward(x)
print("順伝播出力：" + str(a))
da = n.backward(1)
print("逆伝播出力：" + str(da))