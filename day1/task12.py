# -*- coding: utf-8 -*-
"""
Created on Wed Apr 14 14:27:37 2021

@author: takum
"""

f = open('data.txt',encoding = 'UTF-8')

lines = f.readlines()
for i,j in enumerate(lines):
    lines[i] = j.replace("\n","")
    lines[i] = list(map(str,lines[i].split("と")))
f.close() 

  

text = ""

for i in range(len(lines)):
        fruit_text = " ".join(lines[i])
        text += fruit_text + " "
r_text = text.split()    
        
print("docs : " + str(lines))
print("terms : " + str(set(r_text)))