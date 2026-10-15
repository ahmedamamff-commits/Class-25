#create the class, or category for the objects
class Vehicle:

    #Create 'init' method
    def __init__(self, max_speed, mileage):

        #bind the arguments
        self.max_speed = max_speed
        self.mileage = mileage

#Object creation
modelX = Vehicle(240, 18)

#Access the variables inside 'init' method
print("Model Max Speed:", modelX.max_speed)
print("Model mileage", modelX.mileage)