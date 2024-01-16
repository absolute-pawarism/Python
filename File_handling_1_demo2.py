#program: 1
#date: 01/01/2024
#statement: Reading File & Populating list of words which have higher frequency. print 10 such words
string1="Go ahead and drink the other brands served at your neighborhood cafe if you must but make sure you have a stash of Weaver's Peru Organic Whole Bean at home to serve up to your friends and family who deserve the best coffee.  And when you go back to that corner cafe where people drink average coffee because they don't know better, take along a travel mug filled with Weaver's coffee from home and enjoy a real Cup of Joe.  Er, Weaver's. Im learning that Latin American and South American coffees have this distinct \"coffee\" caramelish finish.  As a Peets Coffee fanatics we learned that Weavers roaster was the roaster for Peet's and we are hooked !  I already reviewd the French and Organic blend, but I must say this coffee here is a perfect afternoon drink.Met the weavers team at the Warner Brothers party and they gave me a half a pound of french roast.  Since them we are fans.You wont be dissapointed! Green Mountain is my favorite brand. Nantucket is my favorite coffee from Green Mountain. Very smooth flavor. Not too strong and not too weak. My brother bought me a pound of this coffee for Christmas.  He told me that \"weaver\" was the original roaster for Pete's coffee, he eventually split off and started his own roaster.  Well let me tell you the stuff is delicious!  I've never been married to a brand of coffee, usually would buy the Starbucks 2.5 lb bag at Costco, or whatever looked good at Trader Joes, but Weavers is in a class of it's own.  I'm subscribing to guarantee I can have this stuff delivered to me regularly.  TRY IT!! I keep Regular bags and Decaf bags in my home at all times.Never have to drink old coffee.  Best way to make iced coffee. After having to give up coffee years ago due to a medical condition, I tried many different kinds and favors of tea until I stumbled  upon this in a small bakery that had recently opened nearby. I loved it and have been drinking it every morning since over the past couple of years. The sachets are perfect for a larger mug, the paper wrapped are fine for smaller cups or mugs. It's a hearty tea that I find satisfying and delicious. Looks fresh and clean; I have roasted it in the toaster oven and I also use it in food whole or ground up in the coffee grinder."
word_list=string1.split(" ")
print(len(word_list))
unique_words=set(word_list)
print(len(unique_words))
new_list=[]
for i in unique_words:
    count=0
    if i in word_list:
        count=count+1
        new_list.append(count)   
dictionary_final=dict(map(lambda i,j : (i,j) , unique_words,new_list))
print(dictionary_final)             