# -*- coding: utf-8 -*-
"""
Created on Fri Apr 23 11:02:55 2021

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

a = Perceptron(0.5,0.5,0.7)     #ANDgate
n = Perceptron(-0.5,-0.5,-0.7)  #NANDgate
o = Perceptron(0.5,0.5,0.2)     #ORgate

x1_list = [1, 1, 0, 0]
x2_list = [1, 0, 1, 0]

for i in range(4):
    print("AND(" + str(x1_list[i]) + "," +str(x2_list[i]) + ")=" + str(a.forward(x1_list[i],x2_list[i])),end=" ")
    print("NAND(" + str(x1_list[i]) + "," +str(x2_list[i]) + ")=" + str(n.forward(x1_list[i],x2_list[i])),end=" ")
    print("OR(" + str(x1_list[i]) + "," +str(x2_list[i]) + ")=" + str(o.forward(x1_list[i],x2_list[i])))