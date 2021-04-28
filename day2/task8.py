# -*- coding: utf-8 -*-
"""
Created on Sat Apr 24 17:13:12 2021

@author: takum
"""

import numpy as np

class MLP_3Layer:
    def __init__(self,W1,W2,W3,b1,b2,b3):
        self.W1 = W1
        self.W2 = W2
        self.W3 = W3
        self.b1 = b1
        self.b2 = b2
        self.b3 = b3
    
    def softmax(self,a):
        self.a = a
        c = np.max(self.a,axis=1,keepdims=True)
        exp_a = np.exp(self.a - c)
        sum_exp_a = np.sum(exp_a,axis=1,keepdims=True)
        y = exp_a / sum_exp_a
        return y
        
    def forward(self,x):
        self.x = x
        a1 = np.dot(self.x,self.W1) + self.b1
        z1 = 1 / (1 + np.exp(-a1))
        a2 = np.dot(z1,self.W2) + self.b2
        z2 = 1 / (1 + np.exp(-a2))
        a3 = np.dot(z2,self.W3) + self.b3
        self.softmax(a3)
        
    
x = np.array([[1.0, 0.5], [-0.3, -0.2], [0.0, 0.8], [0.3, -0.4]])
W1 = np.array([[0.1, 0.3, 0.5], [0.2, 0.4, 0.6]])
b1 = np.array([0.1, 0.2, 0.3])
W2 = np.array([[0.1, 0.4], [0.2, 0.5], [0.3, 0.6]])
b2 = np.array([0.1, 0.2])
W3 = np.array([[0.1, 0.3], [0.2, 0.4]])
b3 = np.array([0.1, 0.2])

n = MLP_3Layer(W1, W2, W3, b1, b2, b3)
print(n.forward(x))