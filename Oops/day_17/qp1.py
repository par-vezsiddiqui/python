# Create a class Car with brand and speed (default 0). Add accelerate(amount) and brake(amount) methods that change the speed and print it. Brake must never take the speed below 0.

class Car:
    def __init__(self, brand, speed=0):
        self.brand = brand
        self.speed = speed

    def accelerate(self, amount):
        self.speed += amount
        print("Speed:", self.speed)

    def brake(self, amount):
        self.speed = max(0, self.speed - amount)
        print("Speed:", self.speed)

# Create an instance of the Car class
car = Car("Toyota")

# Test the methods
car.accelerate(50)
car.accelerate(20)
car.brake(30)
car.brake(100)

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
