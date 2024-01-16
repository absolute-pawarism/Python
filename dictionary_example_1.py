# -*- coding: utf-8 -*-
"""
Created on Tue Dec  5 10:16:05 2023

@author: students
"""
thisdict={"brand":"Ford", "model":"Mustang", "year":"1964"}
x=thisdict["model"]
print(thisdict)
print(x)
y=thisdict.get("model")
print(y)
thisdict["year"]=2018
print(thisdict)
#help(dict())
for x in thisdict:
    print(x)
for x in thisdict:
    print(thisdict[x])
for x in thisdict.values():
    print(x)    
    