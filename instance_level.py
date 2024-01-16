# -*- coding: utf-8 -*-
"""
Created on Tue Dec 26 13:42:58 2023

@author: students
"""
class MyClass:
    i=1234
    def f(self):
        return "Hello world"
    
    def __init__(self,name):
        self.name=name
    
    def display(self):
        print("abc")
#    def display():
        
#x=MyClass
#x.counter=1
#while x.counter<10:
 #   x.counter=x.counter*2
#print(x.counter)
#print(x.i)
"""y=MyClass
y.sum=0
while y.sum<10:
    y.sum=y.sum+1"""
#print(y.sum)    
#print(dir(x))
#obj1 = MyClass('harsh')
#obj1.display()
obj2=MyClass()
obj2.display()
#z=MyClass
#print(z.__name__)
#print(x.__dict__)
#print(dir(y))
#print(y.__dict__)
print(MyClass())