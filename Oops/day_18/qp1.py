# Create a class Animal with name and a method speak() that prints the name and makes a sound. Create Dog and Cat as children that override speak(). Put one of each in a list and loop through it.

class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        print(self.name, "makes a sound")

class Dog(Animal):
    def speak(self):
        print(self.name, "says Woof!")

class Cat(Animal):
    def speak(self):
        print(self.name, "says Meow!")

animals = [Dog("Tommy"), Cat("Kitty")]

for animal in animals:
    animal.speak()
