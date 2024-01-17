# -*- coding: utf-8 -*-
"""
Created on Tue Nov 28 13:05:32 2023

@author: students
"""
first_name=['rohit','virat','surya','kl','shreyas','shubhman','ravindra','siraj','kuldeep','shami','jasprit']
#last_name=['sharma','kohli','yadav','rahul','iyer','gill','jadeja','mohd.','yadav','mohd.','bumrah']
def Display_studentlist():
    print(first_name)
    return first_name


def GetStudentCount():
    count=0
    for i in first_name:
        count=count+1
    print(count)
if __name__=='__main__':   
        
    Display_studentlist()
    GetStudentCount()
