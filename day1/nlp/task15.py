# -*- coding: utf-8 -*-
"""
Created on Fri Apr 16 11:18:52 2021

@author: takum
"""

import numpy as np
import task13
import task14

docs = [["リンゴ", "リンゴ"], ["リンゴ", "レモン"], ["レモン", "ミカン"]]
terms = ["リンゴ", "レモン", "ミカン"]

def tfidf(t,d):
    tf = []
    idf = []
    
    for i in range(len(terms)):
        result = []
        for j in range(len(docs)):
            result.append(task13.tf(terms[j],docs[i]))
        tf.append(result)
    
    for i in range(len(terms)):
        idf.append(task14.idf(terms[i],d))

    tf_array = np.array(tf)
    idf_array = np.array(idf)

    return tf_array * idf_array            

print(tfidf(terms,docs))