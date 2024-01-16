# -*- coding: utf-8 -*-
"""
Created on Wed Nov 29 14:41:07 2023

@author: students
"""
stack=[]

def push_op(element):
    stack.append(element)
    print(stack)
    return stack
def pop_op():
    if stack==[]:
        print("stack is empty!")
    else:    
        stack.pop()
    print(stack)
    return stack
def peep_op():
    n=len(stack)
    print(f"topmost element is {stack[n-1]}")
    return stack[n-1]
def search_op(element):
    n2=stack.index(element)
    
    print(f"element is at {n2} position")
    return n2
def empty_or_not():
    if stack==[]:
        print("stack is empty")
        return True
    else:
        print(f"stack has {len(stack)} elements, and its not empty!")
if __name__=='__main__':
    push_op(2)
    push_op(3)
    push_op(4)
    push_op(1)
    push_op(5)
    pop_op()
    peep_op()
    search_op(4)
    print(f"the recent elements are {stack}")
    empty_or_not()


        