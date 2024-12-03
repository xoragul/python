class Dog():
    def __init__(self,sound):
        self.Sound=sound

    def move(self):
        print(f"sound:{self.Sound}")

        
class Cat():
    def __init__(self,sound):
        self.Sound=sound

    def move(self):
        print(f"sound:{self.Sound}")


obj=Dog(" This is dog sound")
obj1=Cat(" This is dog cat sound")


obj.move()
obj1.move()





class Instrument():
    def __init__(self,brand):
        self.Brand=brand
    def move(self):
        print(f"{self.Brand}")

class Guiter():
    def __init__(self,brand):
        self.Brand=brand
    def move(self):
        print(f"{self.Brand}") 

class Drump():
    def __init__(self,brand):
        self.Brand=brand

    def move(self):
        print(f"{self.Brand}")                  
        

obj1=Instrument("one of the feel")
obj2=Guiter("nice sound")
obj3=Drump("rock sound")

obj1.move()
obj2.move()
obj3.move()

        

        
class Dog():
    def __init__(self,noice):
        self.Noice=noice

    def move(self):
        print(f"{self.Noice}")

class Cat():
    def __init__(self,sound):
        self.Sound=sound

    def move(self):
        print(f"{self.Sound}")

obj=Dog("high sound")
obj1=Cat("light sound")

obj.move()
obj1.move()

            
                 







