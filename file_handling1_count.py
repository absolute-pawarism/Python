#program: 1(edited)
#date: 01/01/2024
# Problem statement: Reading file and populating list of words have higher frequency, print 10 such words
import os 
with open("C:\\Users\\Harsh_2\\Downloads\\coffee_reviews.txt","rb") as file:
    String1=file.read().decode()
    #print(String1) 
    word_list=String1.split()
    print(len(word_list))
    unique_words=set(word_list)
    counter_set={}
    #print(len(unique_words))
    for word in unique_words:
        counter=word_list.count(word)
        counter_set.append(counter)
    #print(len(counter_list))
    dictionary_final=dict(map(lambda i,j: (i,j), unique_words,counter_set)) 
    #print(dictionary_final)   
    sorted_dictionary=sorted(dictionary_final.items(), key=lambda x:x[1], reverse=True)
    #print(sorted_dictionary)
    for i in range(10):
        if i<len(sorted_dictionary):
            print(sorted_dictionary[i])
        else:
            break 
