# -*- coding: utf-8 -*-
"""
Created on Fri Apr 23 11:16:11 2021

@author: takum
"""

import numpy as np

def AND(x1,x2):
    x = np.array([x1,x2])
    w = np.array([0.5,0.5])
    b = -0.7
    tmp = np.sum(w*x) + b
    if tmp <= 0:
        return 0
    else:
        return 1
    
def NAND(x1,x2):
    x = np.array([x1,x2])
    w = np.array([-0.5,-0.5])
    b = 0.7
    tmp = np.sum(w*x) + b
    if tmp <= 0:
        return 0
    else:
        return 1

def OR(x1,x2):
    x = np.array([x1,x2])
    w = np.array([0.5,0.5])
    b = -0.2
    tmp = np.sum(w*x) + b
    if tmp <= 0:
        return 0
    else:
        return 1

def XOR(x1,x2):
    s1 = NAND(x1,x2)
    s2 = OR(x1,x2)
    y = AND(s1,s2)
    return y

x1_list = [1, 1, 0, 0]
x2_list = [1, 0, 1, 0]

for i in range(4):
    print("XOR(" + str(x1_list[i]) + "," +str(x2_list[i]) + ")=" + str(XOR(x1_list[i],x2_list[i])))