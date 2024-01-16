import re
pat="a*b"
#match searches only at the beginning
m1=re.match(pat,"abfooaaabcde")
print(m1.group())
m2=re.match(pat,"fooaaabcde")
print("match {}",m2)
m3=re.search(pat,"fooaaabcdeabc")
#search searches at anywhere 
print("Search {}",m3.group())

pat1="\w+@(\w+\.)+(com|org|net|edu)"
r1=re.match(pat1,"finin@cs.umbc.edu")
print(r1.group())

pat2="\w+@(\w+\.)+(com|org|net|edu)"
r2=re.search(pat2,"this email is finin@cs.umbc.edu and another email is datadetectiveharsh@gmail.com")
print(r2.group())

r3=re.split("\W+","This... is a test, short and sweet, of split().")
print(r3)

r4=re.split("\W+","This: is the# 'core' python\'s book")
print(r4)

r5=re.sub('(blue|white|red)','black','blue socks and red shoes')
print(r5)

pat3="\Wa"
pat4="\ba[\w]*\b"
r7=re.split(pat3,"an apple a day keeps doctor away")
print(r7)
r6=re.findall("^a+","an apple a day keeps doctor away")
print(r6)

pat8="\d{1,2}-\d{2}-\d{4}"
string="Tanmay 22 4-02-2002 Alaissa 22 9-01-2002 Ishaan 22 20-02-2002"
r8=re.findall(pat8,string)
print(r8)