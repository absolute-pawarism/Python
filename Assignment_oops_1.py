#define a class called Moblike with the following description 
#instance variables/data members:
class mobike:
    charge=0
    def  __init__(self,bno,phno,name,days):
        self.bno=bno
        self.phno=phno
        self.name=name
        self.days=days
        #self.charge=charge
    def input_details(self):
        self.bno=self.bno
        self.phno=self.phno
        self.name=self.name
        self.days=self.days
        
    def compute(self):
        if self.days<=5:
            mobike.charge=500*self.days
        elif self.days>5 and self.days<=10:
            mobike.charge=400*self.days
        else:
            mobike.charge=200*self.days 
        return self.charge
    def display(self):
        print(f"Bike number is: {self.bno}\nof the owner: {self.name}\nhaving contact no:+91{self.phno}\nfor {self.days} days\nand charges will be: {mobike.charge} rupees. ")           

if __name__=="__main__":
    obj1=mobike("GJ23R6288","9999399993","HARSHAL PAWAR",6)
    obj1.input_details()
    obj1.compute()
    obj1.display()

