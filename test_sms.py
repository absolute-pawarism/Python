# -*- coding: utf-8 -*-
"""
Created on Tue Nov 28 14:24:43 2023

@author: students
"""
from Student_management_system import Student
from Student_management_system import Faculty
from Student_management_system import Placements

print("------- Student List -------")
Student.Display_studentlist()
print("------- Student count -------")
Student.GetStudentCount()
print("------- Faculty Details -------")
Faculty.GetFacultyDetails()
print("------- Faculty for specific Subject -------")
Faculty.FacultyforSubject('mentoring')
print("------- Companies List -------")
Placements.Display_companies()
print("------- Companies from specific Domain -------")
Placements.companiesfromdomain('north')