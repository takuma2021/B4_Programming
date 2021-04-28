# -*- coding: utf-8 -*-
"""
Created on Sat Apr 24 19:35:20 2021

@author: takum
"""

class Multiply():
    def __init__(self):
        """ 逆伝播計算に必要な変数：forwardの⼊⼒値 """
        self.x = None
        self.y = None
    def forward(self, x, y):
        """ 順伝播計算：z = x * y """
        self.x = x
        self.y = y
        z = x * y
        return z
    def backprop(self, dz):
        """ 逆伝播計算: dz/dx = y, dz/dy = x """
        dx = dz * self.y
        dy = dz * self.x
        return dx, dy

class Add():
    def __init__(self):
        """ 逆伝播計算に必要な変数：forwardの⼊⼒値 """
        self.x = None
        self.y = None
    def forward(self, x, y):
        """ 順伝播計算：z = x * y """
        self.x = x
        self.y = y
        z = x + y
        return z
    def backprop(self, dz):
        """ 逆伝播計算: dz/dx = y, dz/dy = x """
        dx = dz + self.y
        dy = dz + self.x
        return dx, dy

a = 2
b=3
c=4

num = Add()
NUM = Multiply()
m = num.forward(a, b)
z = NUM.forward(m, c)
print("順伝播出力：" + str(z))

dz = 1
dm,dc = NUM.backprop(dz)
da,db = num.backprop(dm)
print("逆伝播出力 da:" + str(da) + ",db:" + str(db) + ",dc:" + str(dc))
