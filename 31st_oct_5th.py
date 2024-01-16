L1=[10,20,30]
L2=[30,10,40]
NL=[(x,y) for x in L1 for y in L2 if x!=y]
print(NL)