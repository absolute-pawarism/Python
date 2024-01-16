L1=[]
number=int(input("Enter the value:"))
for i in range(0,number):
    L1.append(input())
print(L1)  
NL=[1 for ch in L1 if ch[0]==ch[-1] and len(ch)>=2]  
print(sum(NL))