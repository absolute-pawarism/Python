# -*- coding: utf-8 -*-
"""
Created on Wed Nov 22 11:12:43 2023

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
for item in a:
    print(item)