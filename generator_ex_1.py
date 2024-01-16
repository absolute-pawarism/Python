# -*- coding: utf-8 -*-
"""
Created on Wed Nov 22 11:02:59 2023

@author: students
"""

def myrange(x,y):
    while x<=y:
        yield x
        x+=1
a=myrange(5, 10)
print(a)
for i in a:
    print(i,end=" ")