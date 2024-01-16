string1="the quick brown fox jumps over the lazy dog"
L1=string1.split(" ")
NL=[x for x in L1 if len(x)>3]
print(NL)