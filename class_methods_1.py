# -*- coding: utf-8 -*-
"""
Created on Tue Dec 26 13:42:57 2023

@author: students
"""

class student:
    def Set_name(self,st_name):
        self.st_name=st_name
    def Set_marks(self,st_marks):
        self.st_marks=st_marks
    def Get_name(self):
        return self.st_name
    def Get_marks(self):
        return self.st_marks


number=int(input("How many students you want to add? ")) 
for i in range(number):
    obj = student()
    name=input("enter name: ")
    obj.Set_name(name)
    marks=input("enter marks: ")
    obj.Set_marks(marks)
    print(obj.Get_name())
    print(obj.Get_marks())
   