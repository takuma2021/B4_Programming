# -*- coding: utf-8 -*-
"""
Created on Wed Apr 14 10:25:21 2021

@author: takum
"""

for i in range(1,31):
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)