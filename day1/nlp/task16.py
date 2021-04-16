# -*- coding: utf-8 -*-
"""
Created on Fri Apr 16 11:27:55 2021

@author: takum
"""

import numpy as np

def cos_sim(v1,v2):
    return np.dot(v1,v2) / (np.sqrt(np.dot(v1,v1)) * np.sqrt(np.dot(v2,v2)))

x1 = np.array([1, 0, 0, 1])
x2 = np.array([0, 1, 0, 1])

print(cos_sim(x1, x2))