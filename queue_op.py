# -*- coding: utf-8 -*-
"""
Created on Mon Dec  4 13:35:45 2023

@author: students
"""
from Queue_op.queue import add_element
from Queue_op.queue import remove_element
from Queue_op.queue import search_element
from Queue_op.queue import is_empty
flag = True
#value=int(input("Harsh is heartly welcomes you to stack program, operations:\n1.Push\n2.Pop\n3.Peep\n4.Search\n5.Empty or not?\n6.Exit   "))
while(flag):
    print("Harsh is heartly welcomes you to queue program, ")
    value=int(input("operations:\n1.Add\n2.Remove\n3.Search\n4.Empty or not?\n5.Exit\nEnter the operation you want to perform: "))
    match value:
        case 1:
            print("1.Add element in queue: ")
            
            element=int(input())
            add_element(element)
        
        case 2:
            remove_element()
        
        case 3:
            print("enter element you want to search: ")
            element2=int(input())
            search_element(element2)
        case 4:
            is_empty()
        case 5:
            print("Exit")
            flag = False
