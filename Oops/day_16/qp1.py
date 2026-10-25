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

car = Car("Toyota")

car.accelerate(50)
car.accelerate(20)
car.brake(30)
car.brake(100)