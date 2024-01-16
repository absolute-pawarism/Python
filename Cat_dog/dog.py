class Dog:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def info(self):
        print(f"I am dog having name {self.name} and {self.age} years old.")

    def make_sound(self):
        print("bark")        
    