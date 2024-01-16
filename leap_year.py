#program to check if given year is leap year or not
def leap_year(year):
    if (year%4==0 and year%100!=0):
        print("given year is leap year")
    else:
        print("not a leap year")
value=int(input("Enter the year: "))
leap_year(value)
       

    
    
        