String_1=input("Enter your String: ")
temp_str=""
for char in String_1:
	if char not in temp_str:
		temp_str=temp_str+char
print(temp_str) l