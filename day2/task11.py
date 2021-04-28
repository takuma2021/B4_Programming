# -*- coding: utf-8 -*-
"""
Created on Sat Apr 24 20:28:03 2021

@author: takum
"""

import numpy as np

class ReLU:
    def __init__(self):
        self.mask = None

    def forward(self, x):
        self.mask = (x <= 0)
        out = x.copy()
        out[self.mask] = 0

        return out

    def backward(self, dout):
        dout[self.mask] = 0
        dx = dout

        return dx
    
    
    
x = np.array([-0.5, 0.0, 1.0, 2.0])
n = ReLU()
a = n.forward(x)
print("順伝播出力：" + str(a))


da = n.backward(a)
print("逆伝播出力：" + str(da))