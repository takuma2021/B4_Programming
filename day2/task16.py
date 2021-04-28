# -*- coding: utf-8 -*-
"""
Created on Sun Apr 25 16:47:47 2021

@author: takum
"""

import sys,os
sys.path.append(os.pardir)
from common.functions import *
from common.gradient import numerical_gradient

class NeuralNetwork():
    def __init__(self,input_size,hidden_size,output_size,weight_init_std=0.01):
        #重みの初期化
        self.params = {}
        self.params['W1'] = weight_init_std *  np.random.randn(input_size,hidden_size)
        self.params['b1'] = np.zeros(hidden_size)
        self.params['W2'] = weight_init_std * np.random.randn(hidden_size,output_size)
        self.params['b2'] = np.zeros(output_size)
        
    def forward(self,x):
        W1,W2 = self.params['W1'],self.params['W2']
        b1,b2 = self.params['b1'],self.params['b2']
        
        a1 = np.dot(x,W1) + b1
        z1 = sigmoid(a1)
        a2 = np.dot(z1,W2) + b2
        y = sofgmax(a2)
        
        return y
    
    def loss(self,x,t):
        y = self.forward(x)
        
        return coross_entropy_error(y,t)
    
    def accuracy(self,x,t):
        y = self.forward(x)
        y = np.argmax(y,axis=1)
        y = np.argmax(t,axis=1)
        
        accuracy = np.sum(y == t) / float(x.shape[0])
        return accuracy
    
    def numerical_gradient(self,x,t):
        loss_W = lambda W :self.loss(x,t)
        
        grads = {}
        grads['W1'] = numerical_gradient(loss_W,self.params['W1'])
        grads['b1'] = numerical_gradient(loss_W,self.params['b1'])
        grads['W2'] = numerical_gradient(loss_W,self.params['W2'])
        grads['b2'] = numerical_gradient(loss_W,self.params['b2'])
        
        return grads
    

net = NeuralNetwork(784, 500, 10)
net.params['W1'].shape
net.params['b1'].shape
net.params['W2'].shape
net.params['b2'].shape

x = np.random.rand(100,784)
t = np.random.rand(100,10)

grads = net.numerical_gradient(x, t) #勾配を計算

grads['W1'].shape 
grads['b1'].shape 
grads['W2'].shape 
grads['b2'].shape 