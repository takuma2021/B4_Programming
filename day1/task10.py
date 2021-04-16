# -*- coding: utf-8 -*-
"""
Created on Wed Apr 14 14:01:23 2021

@author: takum
"""

import sys

args = sys.argv
args.pop(0)
text = " ".join(map(str,args))


def word_n_gram(text,N):
    words = text.split()
    result = []
    for i,c in enumerate(words):
        if i+N > len(words):
            return result
        result.append(words[i:i+N])

#text = "I am an NLPer"
print(word_n_gram(text, 2))