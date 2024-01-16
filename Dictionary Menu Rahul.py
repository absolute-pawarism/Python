
def menu():
    print ("Press 1 for adding data ")
    print ("Press 2 for updating data")
    print ("Press 3 for delete data")
    print ("Press 4 for display data")

def submenu():
    print ("Press 1 for changing capital   ")
    print ("Press 2 for changing flower  ")



def add_data():
    county= input("country_name : ")
    capital= input("capital : ")
    flower= input("flower : ")
    data={}
    data["capital"]= capital
    data["flower"]= flower
    country_data[county]=data
    print(country_data)
    
def update_data():
    print("update")
    country= input("Enter the country data change : ")
    submenu()
    choice = int(input("Enter the choice : "))
    match choice:
        case 1:
            capital = input("Enter the capital name : ")
            country_data[country]['capital']=capital
            
        case 2:
            flower = input("Enter the flower name : ")
            country_data[country]['flower']=flower
    print(country_data[country])


def delet_data() :
    print("delete")
    country= input("which county you want to list delete : ")
    del country_data[country]
    print(country_data)


country_data ={}
while(True):
    menu()
   
    choice = int(input("Enter the choice: "))
    match choice:
        case 1: 
            add_data()
            
        case 2:
            update_data()          
            
        case 3:
            delet_data()
            
        case 4: 
            print("display")
            print(country_data)    
            
        case 5: break
        
        
