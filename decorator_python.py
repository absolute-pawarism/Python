# -*- coding: utf-8 -*-
"""
Created on Wed Nov 22 14:35:30 2023

@author: students
"""

def make_pretty(func):
    def inner():
        print("i got decorated")
        func()
    return inner
    
@make_pretty
def ordinary():
    print("i am ordinary")

ordinary()

        