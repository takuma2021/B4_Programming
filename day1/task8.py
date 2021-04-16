# -*- coding: utf-8 -*-
"""
Created on Wed Apr 14 11:06:02 2021

@author: takum
"""

text = "Hi He Lead Because Boron Could Not Oxidize Flourine. New Nations Might Also Sign Peace Security Clause. Arthur King Can."
head = [1,5,6,7,8,9,15,16,19]
dic = {}
words = text.split()

for i,word in enumerate(words):
    if i+1 in head:
        dic[i+1] = word[0]
    else:
        dic[i+1] = word[:2]
        
print(dic)