# -*- coding: utf-8 -*-
"""
Created on Tue Jan  9 13:43:36 2024

@author: students
"""

#write a program to showcase multiple inheritance
class clock:
    def __init__(self,hrs=0,minute=0,sec=0):
        self.hrs=hrs
        self.minute=minute
        self.sec=sec
    def set_clock(self,hrs,minute,sec):
        self.hrs=hrs
        self.minute=minute
        self.sec=sec    
    def tick(self):
        self.sec=self.sec+1
        if self.sec>=60:
            self.sec=self.sec-60
            self.minute=self.minute+1
            
        if self.minute>60:
            self.minute=self.minute-60
            self.hrs=self.hrs+1
                 
        print(f"{self.hrs}:{self.minute}:{self.sec}")
class calender:
    def __init__(self,day=1,month=1,year=1995):
        self.day=day
        self.month=month
        self.year=year
    def set_calender(self,day,month,year):
        self.day=self.day
        self.month=month
        self.year=year
    def advance(self):
        self.day=self.day+1
        if self.day>31:
            self.day=self.day-31
            self.month=self.month+1
        elif self.day>28:
            self.day=self.day-28
            self.month=self.month+1 
        elif self.day>30:
            self.day=self.day-30
            self.month=self.month+1       
        if self.month>12:
            self.month=self.month-12
            self.year=self.year+1
            if (self.year % 400 == 0) and (self.year % 100 == 0):
                print(f"{self.year} is a leap year")

            # not divided by 100 means not a century year
# year divided by 4 is a leap year
            elif (self.year % 4 ==0) and (self.year % 100 != 0):
                    print(f"{self.year} is a leap year")

            # if not divided by both 400 (century year) and 4 (not century year)
# year is not leap year
            else:
                    print(f"{self.year} is not a leap year") 
        print(self.day,self.month,self.year)               
    def display(self):
         date_in_string=str(self.day)+"/"+str(self.month)+"/"+str(self.year)
         print(date_in_string)
class calenderclock(calender,clock):
    def __init__(self,hrs=0,minute=0,sec=0,day=1,month=1,year=2000):
        clock.__init__()
        calender.__init__()
        
    def tick(self):
        super().tick()
        if clock.hrs>12:
            clock.hrs=clock.hrs-12
            calender.day=calender.day+1
            calender.advance()
        else:
            calender.day=calender.day+1
            calender.advance()    


obj3=calenderclock(12,59,59,31,12,2023)
obj3.tick()


               