# -*- coding: utf-8 -*-
"""
Created on Wed Dec 20 14:02:30 2023

@author: students
"""

l3={}
sampleDict={"name":"kelly",
            "age":25,
            "salary":8000,
            "city":"New york"}
l1=[]
l2=[]
for i in sampleDict.keys():
    l2.append(i)
for j in sampleDict.values():
    l1.append(j) 
l2[3]='location'
    
new=dict(map(lambda x,y: {x,y},l1,l2))
print(new)