#date:2/1/24
#problem statement: Write a python program to create a vehicle class with max_speed and mileage instance attributes
class vehicle:
    color="white"
    def __init__(self,max_speed,mileage):
        self.max_speed=max_speed
        self.mileage=mileage
    def fare(self,fare,final_fare):
        self.fare=self.capacity*100
            
    
class bus(vehicle):
    def __init__(self,max_speed,mileage,type):
        super().__init__(self,max_speed,mileage)
        self.capacity=50
        self.type=type
        print(f"Bus is heavy vehicle.")

        print(f"Bus has {super().color} color. ")
    def fare(self):
        self.fare=super().self.fare
        self.final_fare=self.fare+(self.fare*(10/100))
        

class car(vehicle):
    def __init__(self,max_speed,mileage,capacity,type,seats):
        super().__init__(self,max_speed,mileage)
        self.capacity=7
        self.type=type
        self.seats=seats
        print(f"car is light vehicle.")
        color=vehicle.color
        print(f"car has {color} color. ")
    def fare(self,fare,final_fare):
        self.fare=super().self.fare
        print(f" fare for car is {self.final_fare}") 


volvo_bus=bus(250,25,"volvo")
volvo_bus.fare()

