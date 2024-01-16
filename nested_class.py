# -*- coding: utf-8 -*-
"""
Created on Tue Dec 26 15:40:22 2023

@author: students
"""
class person:
    def __init__(self,name,dob):
        
        self.name=name
        dd,mm,yy=dob.split("-")        
        self.dob=self.DOB(dd,mm,yy)
        
        
    def display(self):
        #print(self.name)
        #self.dob.display()
        print(f"name is: {self.name}, dob is: {self.dob.display()}")
        
    class DOB:
        def __init__(self,dd,mm,yy):
            self.dd,self.mm,self.yy=dd,mm,yy            
                       
        def display(self):
            return f"{self.dd}/{self.mm}/{self.yy}"
            


            
class demo:
    def my_method(obj):
        return obj.display()
