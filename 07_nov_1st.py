# -*- coding: utf-8 -*-
"""
Created on Tue Nov  7 14:59:30 2023

@author: students
"""

def fact(number):
    if number>0:
        return number * fact(number-1)
    return 1
magic_sum=0
value=int(input("Enter the number: "))
temp_value=value
while(value>0):
    reminder=value%10
    value=int(value/10)
    magic_sum=magic_sum+fact(reminder)

  

print(magic_sum)
if magic_sum==temp_value:
    print("whoa...its magic number...")
else:
    print("sorry, its not a  magic number.")
          
        
    
    
