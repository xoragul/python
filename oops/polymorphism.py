
class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def move(self):
        print(f"Drive the: {self.brand} {self.model}!")

class Boat:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def move(self):
        print(f"Sail the :{self.brand} {self.model}!")

class Plane:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def move(self):
        print(f"Fly the: {self.brand} {self.model}!")

car1 = Car("Ford", "Mustang")       
boat1 = Boat("Ibiza", "Touring 20") 
plane1 = Plane("Boeing", "747")    

car1.move()   
boat1.move()  
plane1.move() 


