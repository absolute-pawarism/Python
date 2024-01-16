# -*- coding: utf-8 -*-
"""
Created on Thu Jan  4 16:08:41 2024

@author: students
"""

import math
from abc import ABC, abstractmethod
class shape(ABC):
    def __init__(self, area):
        self.area=area
        print("area")
            
    @abstractmethod
    def area(self):
        
        pass

class circle(shape):
    def __init__(self,r):
        self.r=r
        
    
    def area(self):
        self.area=math.pi*self.r*self.r
        print(self.area)


class ractangle(shape):
    def __init__(self,l,b,h):
        self.l=l
        self.b=b
        self.h=h
        
    def area(self):
        self.area=self.l*self.b*self.h
        print(self.area)  

obj1=circle(4)
obj1.area()
obj2=ractangle(2,4,5)
obj2.area()
