number=int(input("how many numbers you want in your list? : "))
L1=[]
temp_list=[]
for i in range(0,number):
   L1.append(input())
print(L1)   

value=input("Enter the value you want to search: ")   
count=0   
pos=0
for char in L1:
    if char==value:
        pos = L1.index(char,pos)
        temp_list.append(pos)
        count=count+1
        pos=pos+1
print(f"index at which element is:{temp_list}")
print(f"value is {value} is occured {count} times")        
        
        
    
        