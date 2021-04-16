# -*- coding: utf-8 -*-
"""
Created on Fri Apr 16 11:36:55 2021

@author: takum
"""

import numpy as np
from nlp import task15,task16

docA = ['リンゴ', 'リンゴ', 'リンゴ'] 
docB = ['リンゴ', 'レモン', 'レモン', 'ミカン']
docC = ['リンゴ', 'イチゴ', 'ミカン']
docD = ['レモン', 'イチゴ', 'ミカン']
docE = ['ミカン', 'ミカン', 'ブドウ', 'ブドウ']

#リンゴ、レモン、ミカン、イチゴ、ブドウの個数
ndocA = np.array([3,0,0,0,0]) #リンゴ3つ
ndocB = np.array([1,2,1,0,0]) #リンゴ1,レモン2,ミカン1
ndocC = np.array([1,0,1,1,0]) #リンゴ1,イチゴ1,ミカン1
ndocD = np.array([0,1,1,1,0]) #レモン1,イチゴ1,ミカン1
ndocE = np.array([0,0,2,0,2]) #ミカン2,ブドウ2

result = np.zeros((5,5))

result[0][0] = (task16.cos_sim(ndocA,ndocA))
result[0][1] = (task16.cos_sim(ndocA,ndocB))
result[0][2] = (task16.cos_sim(ndocA,ndocC))
result[0][3] = (task16.cos_sim(ndocA,ndocD))
result[0][4] = (task16.cos_sim(ndocA,ndocE))

result[1][0] = (task16.cos_sim(ndocB,ndocA))
result[1][1] = (task16.cos_sim(ndocB,ndocB))
result[1][2] = (task16.cos_sim(ndocB,ndocC))
result[1][3] = (task16.cos_sim(ndocB,ndocD))
result[1][4] = (task16.cos_sim(ndocB,ndocE))

result[2][0] = (task16.cos_sim(ndocC,ndocA))
result[2][1] = (task16.cos_sim(ndocC,ndocB))
result[2][2] = (task16.cos_sim(ndocC,ndocC))
result[2][3] = (task16.cos_sim(ndocC,ndocD))
result[2][4] = (task16.cos_sim(ndocC,ndocE))

result[3][0] = (task16.cos_sim(ndocD,ndocA))
result[3][1] = (task16.cos_sim(ndocD,ndocB))
result[3][2] = (task16.cos_sim(ndocD,ndocC))
result[3][3] = (task16.cos_sim(ndocD,ndocD))
result[3][4] = (task16.cos_sim(ndocD,ndocE))

result[4][0] = (task16.cos_sim(ndocE,ndocA))
result[4][1] = (task16.cos_sim(ndocE,ndocB))
result[4][2] = (task16.cos_sim(ndocE,ndocC))
result[4][3] = (task16.cos_sim(ndocE,ndocD))
result[4][4] = (task16.cos_sim(ndocE,ndocE))


print(result)
#if __name__ == "__main__":
#    print(task16.cos_sim(task15.tfidf,task15.tfidf))