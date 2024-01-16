# -*- coding: utf-8 -*-
"""
Created on Wed Nov  8 12:09:47 2023

@author: students
"""
def is_prime(number):
    if(number%1==0 and number%number==0):
        print("prime")
    else:
        print("not prime!")
n=int(input("Enter your value within range(0-20): "))
while(n>0 and n<=20):
    is_prime(n)
        
        
