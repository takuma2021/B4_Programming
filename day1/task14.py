# -*- coding: utf-8 -*-
"""
Created on Fri Apr 16 10:56:46 2021

@author: takum
"""


from math import log
import pandas as pd
import numpy as np

docs = [["リンゴ", "リンゴ"], ["リンゴ", "レモン"], ["レモン", "ミカン"]]
terms = ["リンゴ", "レモン", "ミカン"]



def idf(t,d):
    df = 0
    n = len(docs)
    for doc in docs:
        df += t in doc
    return np.log10(n / df) + 1

for t in terms:
    print("idf(",t,")=",idf(t,docs))
