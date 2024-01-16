# -*- coding: utf-8 -*-
"""
Created on Tue Nov 28 13:05:50 2023

@author: students
"""
#Faculty_assigned_subject=[]
faculty_name=['sachintendulkar','msdhoni','zahirkhan','ravishastri']
def GetFacultyDetails():
    print(faculty_name)
    return faculty_name

subjName=['batting','bowling','kipping','mentoring']

def FacultyforSubject(subjName):
    for i in subjName:
        if subjName=='batting':
            print(f"faculty for batting is: {faculty_name[0]}")
            return faculty_name[0]
        elif subjName=='bowling':
            print(f"faculty for bowling is: {faculty_name[2]}")
            return faculty_name[2]
        elif subjName=='kipping':
            print(f"faculty for kipping is: {faculty_name[1]}")
            return faculty_name[1]
        else:
            print(f"faculty for mentoring is: {faculty_name[3]}")
            return faculty_name[3]

if __name__=='__main__':
    GetFacultyDetails()
    FacultyforSubject('kipping')     
    FacultyforSubject('bowling')
    FacultyforSubject('batting') 
    FacultyforSubject('mentoring')
            
    
    
