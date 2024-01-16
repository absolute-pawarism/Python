# -*- coding: utf-8 -*-
"""
Created on Wed Dec 20 12:47:59 2023

@author: students
"""
#set B
l1=[]
l2=[]
l3=[]
numbers=eval(input("enter the numbers:"))
target_sum=int(input("enter the target sum: "))
for i in numbers:
    for j in numbers:
        if target_sum==i+j:
            l1.append(i)
            l2.append(j)


l3=map(lambda x,y: (x,y),l1,l2)
print(list(l3))
        
        
              
