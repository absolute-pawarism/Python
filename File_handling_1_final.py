#program: 1
#date: 01/01/2024
#statement: Reading File & Populating list of words which have higher frequency. print 10 such words
import os
with open("C:\\Users\\students\\Downloads\\coffee_reviews.txt", "rb") as file:
    String1=file.read().decode()
    #print(String1)
    word_list=String1.split()
    print(len(word_list))
    unique_words=set(word_list)
    #print(len(unique_words))
    new_list=[]
    for i in unique_words:
        count=0
        for j in word_list:
            if i==j:
                count=count+1
        new_list.append(count)   
    dictionary_final=dict(map(lambda i,j : (i,j) , unique_words,new_list))
    sorted_dictionary=sorted(dictionary_final.items(), key=lambda x:x[1], reverse=True)
    #print(sorted_dictionary)
    for i in range(10):
        if i< len(sorted_dictionary):
            print(sorted_dictionary[i])
        else:
            break   



