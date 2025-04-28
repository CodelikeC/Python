#do problem 11 on page 133 
#--------------------------#
#Name : Nguyen Duc Tri 
#Course : CS 2220

print ("Problem 11")
print ("Page 133")

class Vehicle: #base class 
    def __init__(self, make, model, year, color): #function
        self.make = make
        self.model = model
        self.year = year
        self.color = color
        self.is_running = False

    def start(self): #function 
        self.is_running = True
        print(f"The {self.color} {self.make} {self.model} has started.")

    def stop(self): #function
        if self.is_running:
            self.is_running = False
            print(f"The {self.color} {self.make} {self.model} has stopped.")
        else:
            print(f"The {self.color} {self.make} {self.model} is already stopped.")

class Car(Vehicle): #derived class 
    def __init__(self, make, model, year, color, num_doors):
        super().__init__(make, model, year, color) #just like override in C++ 
        self.num_doors = num_doors

    def honk(self):
        print(f"The {self.color} {self.make} {self.model} goes 'Beep beep!'")

# Creating an instance of Vehicle class
my_vehicle = Vehicle("Toyota", "Camry", 2022, "blue")

# Using methods of Vehicle class
my_vehicle.start()
my_vehicle.stop()

# Creating an instance of Car class
my_car = Car("Honda", "Accord", 2023, "red", 4)

# Using methods of both Vehicle and Car classes
my_car.start()
my_car.honk()
my_car.stop()








