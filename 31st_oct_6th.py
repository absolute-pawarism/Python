String1="the quick brown fox jumps over the lazy dog"
L1=String1.split(" ")
print(L1)
NL=[len(x) for x in L1 if x!="the"]
print(NL)