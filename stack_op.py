# -*- coding: utf-8 -*-
"""
Created on Wed Nov 29 15:43:56 2023

@author: students
"""

from stack.stack import pop_op
from stack.stack import push_op
from stack.stack import peep_op
from stack.stack import search_op
from stack.stack import empty_or_not
flag = True
#value=int(input("Harsh is heartly welcomes you to stack program, operations:\n1.Push\n2.Pop\n3.Peep\n4.Search\n5.Empty or not?\n6.Exit   "))
while(flag):
    print("Harsh is heartly welcomes you to stack program, ")
    value=int(input("operations:\n1.Push\n2.Pop\n3.Peep\n4.Search\n5.Empty or not?\n6.Exit\nEnter the operation you want to perform: "))
    match value:
        case 1:
            print("1. Push enter element in stack:")
            
            element=int(input())
            push_op(element)
        
        case 2:
            pop_op()
        case 3:
            peep_op()
        case 4:
            print("enter element you want to search: ")
            element2=int(input())
            search_op(element2)
        case 5:
            empty_or_not()
        case 6:
            print("Exit")
            flag = False
    
