# -*- coding: utf-8 -*-
"""
Created on Wed Apr 14 14:22:59 2021

@author: takum
"""

f = open('data.txt',encoding = 'UTF-8')

data = f.read()
print(data)

f.close()