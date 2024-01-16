# -*- coding: utf-8 -*-
"""
Created on Wed Nov  8 12:39:18 2023

@author: students
"""
n=[1,2,3,4,5]
print("original list:",n)
def f(x):
    x.pop()
    x.pop()
    x.insert(0,0)
    print("Inside f(): ",x)
f(n)
print("after function call:",n)    
