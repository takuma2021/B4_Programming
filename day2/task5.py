# -*- coding: utf-8 -*-
"""
Created on Fri Apr 23 11:43:15 2021

@author: takum
"""

import numpy as np

def relu(x):
    return np.maximum(0,x)

x = np.array([-1.0, 0.0, 0.5, 2.0])
print(relu(x))