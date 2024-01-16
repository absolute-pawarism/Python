#write a program to showcase multiple inheritance
class clock:
    def __init__(self,hrs,minute,sec):
        self.hrs=hrs
        self.minute=minute
        self.sec=sec
    def set_clock(self):
        self.hrs=0
        self.minute=0
        self.sec=0    
    def tick(self):
        self.sec=self.sec+1
        if self.sec>60:
            self.sec=self.sec-60
            self.minute=self.minute+1
        else:
            self.minute=self.minute+1     
        if self.minute>60:
            self.minute=self.minute-60
            self.hour=self.hour+1
        else:
            self.minute=self.minute+1          
        return self.sec, self.minute, self.hour
class calender:
    def __init__(self,day,month,year):
        self.day=day
        self.month=month
        self.year=year
    def set_calender(self):
        self.day=0
        self.month=0
        self.year=0
    def advance(self):
        self.day=self.day+1
        if self.day>31:
            self.day=self.day-31
            self.month=self.month+1
        elif self.day>28:
            self.day=self.day-28
            self.month=self.month+1 
        else:
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
        return self.day,self.month,self.year               
    def display(self):
         date_in_string=str(self.day)+"/"+str(self.month)+"/"+str(self.year)
         return date_in_string
class CalenderClock(calender,clock):
    def tick(self):
        super().tick()
        if clock.hour>12:
            clock.hour=clock.hour-12
            calender.day=calender.day+1
            calender.advance()
        else:
            calender.day=calender.day+1
            calender.advance()    

obj1=CalenderClock(12,14,50) 
obj1.set_clock()
obj1.set_calender()
obj1.display()               