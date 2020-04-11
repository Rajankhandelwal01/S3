class Car:
    wheels = 4 # CLASS Namespace
    def __init__(self):   #Instance Namespace
        self.mil = 10
        self.com = "BMW"

c1 = Car()
c2 = Car()

c1.mil = 8
Car.wheels =5

print(c1.com, c1.mil,Car.wheels)
print(c2.com, c2.mil, Car.wheels)