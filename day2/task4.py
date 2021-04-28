# -*- coding: utf-8 -*-
"""
Created on Fri Apr 23 11:38:53 2021

@author: takum
"""

import numpy as np

def sigmoid(x):
    return 1 / (1 + np.exp(-x))

x = np.array([-1.0, 0.0, 0.5, 2.0])
print(sigmoid(x))