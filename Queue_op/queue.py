# -*- coding: utf-8 -*-
"""
Created on Mon Dec  4 12:56:51 2023

@author: students
"""
queue=[]
def add_element(element):
    queue.append(element)
    print(queue)
    return queue
def remove_element():
    queue.pop(0)
    print(queue)
    return queue
def search_element(element):
    if queue==[]:
        print("queue is empty!")
    else:
        print(f"{element} is at {queue.index(element)} position")
def is_empty():
    if queue==[]:
        print("queue is empty!")
    else:
        print(f"queue is not empty: {queue}")
        return queue
if __name__=='__main__':
    add_element(5)
    add_element(6)
    add_element(7)
    add_element(8)
    remove_element()
    remove_element()
    search_element(8)
    is_empty()        
       
