# -*- coding: utf-8 -*-
"""
Created on Tue Dec  5 10:42:55 2023

@author: students
"""
data=eval(input("enter your data: "))

'''initial=0
for value in data.values():
     sum_op=initial+int(value)  
     initial=sum_op
print(sum_op/len(data.values()))    
'''

total=sum(data.values())
avg=(total/len(data))
print(f"average is: {avg} ")
    
