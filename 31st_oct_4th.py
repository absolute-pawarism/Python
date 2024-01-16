L1=[]
number=int(input("How many numbers you want to enter? "))
for i in range(0,number):
    L1.append(input("Enter the number: "))
print(L1)
NL=[int(x)**3 for x in L1]
print(NL)
  
