#Create Car class
class Car:
#Create class constructor for the car's year make
    def __init__(self, year_model, make):
        self.__year_model = year_model
        self.__make = make
        self.__speed = 0
#Create a class for car's accelerating speed value
    def accelerate(self):
        self.__speed += 5
#Create a class for car's braking speed value
    def brake(self):
        self.__speed -= 5
#Create a getter method for the car speed
