# -*- coding: utf-8 -*-
"""
Created on Fri Apr 16 10:26:59 2021

@author: takum
"""

from math import log
import pandas as pd

docs = [["リンゴ", "リンゴ"], ["リンゴ", "レモン"], ["レモン", "ミカン"]]
terms = ["リンゴ", "レモン", "ミカン"]

n = len(docs)

def tf(t,d):
    return d.count(t) / len(d)

result = []
for i in range(n):
    result.append([])
    d = docs[i]
    for j in range(len(terms)):
        t = terms[j]
        
        result[-1].append(tf(t,d))

for i in range(n):
    for j in range(len(terms)):
        print("tf(" + str(terms[i]) + "," + str(docs[0]) + ") = " + str(result[j][i]))