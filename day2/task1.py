# -*- coding: utf-8 -*-
"""
Created on Fri Apr 23 10:12:56 2021

@author: takum
"""

class Perceptron:
    def __init__(self,w1,w2,theta):
        self.w1 = w1
        self.w2 = w2
        self.theta = theta
    def forward(self,x1,x2):
        self.x1 = x1
        self.x2 = x2
        tmp = self.w1 * self.x1 + self.w2 * self.x2
        if tmp < self.theta:
            return 0
        elif tmp >= self.theta:
            return 1


        
        