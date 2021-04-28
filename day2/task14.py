# -*- coding: utf-8 -*-
"""
Created on Sat Apr 24 21:02:05 2021

@author: takum
"""

import numpy as np

class SoftmaxWithLoss:
    def __init__(self):
        self.loss = None
        self.y = None # softmaxの出力
        self.t = None # 教師データ

    def softmax(self,a):
        self.a = a
        c = np.max(self.a,axis=1,keepdims=True)
        exp_a = np.exp(self.a - c)
        sum_exp_a = np.sum(exp_a,axis=1,keepdims=True)
        y = exp_a / sum_exp_a
        return y
    
    def cross_entropy_error(self,y,t):
        if y.ndim == 1:
            t = t.reshape(1,t.size)
            y = y.reshape(1,y.size)
        bath_size = y.shape[0]
        return -np.sum(t * np.log(y)) / bath_size

    def forward(self, x, t):
        self.t = t
        self.y = self.softmax(x)
        self.loss = self.cross_entropy_error(self.y, self.t)
        
        return self.loss

    def backward(self, dout=1):
        batch_size = self.t.shape[0]
        dx = (self.y - self.t) / batch_size
        
        return dx
x = np.array([[1.0, 0.5], [-0.4, 0.1]])
t = np.array([[1.0, 0.0], [0.0, 1.0]])

n = SoftmaxWithLoss()
a = n.forward(x, t)
print(a)