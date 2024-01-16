# -*- coding: utf-8 -*-
"""
Created on Wed Dec 20 12:48:00 2023

@author: students
"""
l3={}
sampleDict={"name":"kelly",
            "age":25,
            "salary":8000,
            "city":"New york"}
keys=eval(input("enter the keys to extract:"))
l3={i:sampleDict.get(j) for i in keys for j in sampleDict.keys() if i==j}

print(l3)

 

