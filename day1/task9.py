# -*- coding: utf-8 -*-
"""
Created on Wed Apr 14 11:17:42 2021

@author: takum
"""
import random,sys

args = sys.argv
args.pop(0)
text = "".join(map(str,args))

def typoglycemia(text):
    
    def random_word(word):
       if len(word) < 4:  # 3文字以下はそのまま 
           return word
       arr = list(word[1:-1])
       random.shuffle(arr)
       return word[0] + "".join(arr) + word[-1]
    
    return " ".join(list(map(random_word,text.split())))
   


#text = "こんにちは みなさん おげんき ですか ? わたしは げんき です 。"
print(typoglycemia(text))