# OOP Concept: Class & Object
# Defining a base class 'Vehicle'
class Vehicle:
    # OOP Concept: Constructor (__init__) - Used to initialize objects
    def __init__(self, brand, model):
        self.brand = brand  # Attribute to store vehicle brand
        self.model = model  # Attribute to store vehicle model
    
    # Method to display vehicle information
    def show_info(self):
        print(f"Vehicle: {self.brand} {self.model}")

# OOP Concept: Inheritance (Car class inherits from Vehicle)
class Car(Vehicle):
    # Method overriding (show_info method is redefined for Car)
    def show_info(self):
        print(f"Car: {self.brand} {self.model}")

# OOP Concept: Inheritance (Bike class inherits from Vehicle)
class Bike(Vehicle):
    # Method overriding (show_info method is redefined for Bike)
    def show_info(self):
        print(f"Bike: {self.brand} {self.model}")

# Creating objects of Car and Bike classes
car = Car("Toyota", "Camry")  # Car object
bike = Bike("Yamaha", "R15")   # Bike object

# OOP Concept: Polymorphism (Same method name behaves differently in each class)
car.show_info()  # Calls show_info() from Car class
bike.show_info() # Calls show_info() from Bike class
