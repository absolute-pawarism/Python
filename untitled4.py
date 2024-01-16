# -*- coding: utf-8 -*-
"""
Created on Wed Dec 20 14:12:34 2023

@author: students
"""

l3={}
sampleDict={"name":"kelly",
            "age":25,
            "salary":8000,
            "city":"New york"}
if 'city' in sampleDict:
    sampleDict['location']=sampleDict.pop('city')
print(sampleDict) 