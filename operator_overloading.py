class student:
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks
    def __gt__(self,other):
        return (self.marks>other.marks)
obj1=student("Harsh",50)
obj2=student("umang",49)
print(obj1>obj2)