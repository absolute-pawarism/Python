from Cat_dog.cat import Cat
from Cat_dog.dog import Dog

cat1=Cat("Kitty", 2.5)
dog1=Dog("Fluffy", 4)

for animal in (cat1,dog1):
        animal.make_sound()
        animal.info()