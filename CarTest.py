#Import the main program
from Car import *

#Create a class for testing
class CarTest:
#Create a method for testing
    def main():
#Create an object with the car's year and make
        my_car = Car(2020, "Chevrolet")
       
#Call the accelerate method using for loop
        for i in range(5):
            my_car.accelerate()
            print("Current speed after accelerating:", my_car.get_speed())

#Call the brake method using for loop
        for i in range(5):
            my_car.brake()
            print("Current speed after braking:", my_car.get_speed())
                  
#Start the test program
