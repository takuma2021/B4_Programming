# -*- coding: utf-8 -*-
"""
Created on Wed Apr 14 10:45:56 2021

@author: takum
"""

text = "Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics."
text1 = text.replace(',','')
text2 = text1.replace('.','')
text3 = text2.split()
n = len(text3)
list = []

for i in range(n):
    list.append(len(text3[i]))

print(list)