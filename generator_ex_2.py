# -*- coding: utf-8 -*-
"""
Created on Wed Nov 22 11:05:12 2023

@author: students
"""

def my_gen():
    n=1
    print("this is printed first")
    yield n
    
    n+=1
    print("this is printed second")
    yield n
    
    n+=1
    print("this is printed at last")
    yield n
a=my_gen()
print(next(a))
print(next(a))
print(next(a))
#next(a)