# -*- coding: utf-8 -*-
"""
Created on Fri Apr 23 10:25:52 2021

@author: takum
"""

import numpy as np

class Perceptron:
    def __init__(self,w1,w2,theta):
        self.w = np.array([w1,w2]).reshape(2,1)
        self.theta = theta
    def forward(self,x1,x2):
        self.x = np.array([x1,x2])
        tmp = np.sum(self.w * self.x)
        if tmp < self.theta:
            return 0
        elif tmp >= self.theta:
            return 1

a = Perceptron(0.5,0.5,0.7)     #ANDgate
n = Perceptron(-0.5,-0.5,-0.7)  #NANDgate
o = Perceptron(0.5,0.5,0.2)     #ORgate

x1_list = [1,1,0,0]
x2_list = [1,0,1,0]

print(a.forward(x1_list,x2_list))
print(n.forward(x1_list,x2_list))
print(o.forward(x1_list,x2_list))
