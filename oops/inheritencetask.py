
# class Animal:
#     def name (self):
#         print("animal eat food")


# class Dog(Animal):
#     def name1(self):
#         print("animal")

# obj=Dog()
# obj.name()


# class Vehicle:
#     def name (self):
#         print("move the car")

# class Car(Vehicle):
#     def name1(self):
#         print("move it car")

# obj=Car()
# obj.name()



# class Animal:
#     def name1(self):
#         print("bark the dog")

# class Dog(Animal):
#     def name2(self):
#         print("DOG")

# obj=Dog()
# obj.name1()





# class Bird:
#     def name1(self):
#         print("penguins can't fly")


# class Penguine(Bird):
#     def name2(self):
#         print("penguine is a bird")

# obj=Penguine()
# obj.name1()





# class Shape:
#     def name(self):
#         print("implement this method")

# class Squere(Shape):
#     def __init__(self,lenth):
#         self.Lenth=lenth

#     def area (self):
#         return  self.Lenth**2
    

# obj=Squere(4)
# print(f"{obj.area()}")



# class Grandparent:
#     def name1(self):
#         print("hello from grandparent")

# class Parent(Grandparent):
#     def name2(self):
#         print("hello from parent")

# class Child(Parent):
#     def name3(self):
#         print("hello from child")

# obj=Child()
# obj.name2()



# class Fruits:
#     def name1(self):
#         print("color")

# class Apple(Fruits):
#     def name2(self):
#         print("red")

# class Banana(Apple):
#     def name3(self):
#         print("yellow")


# obj=Banana()

# obj.name1()





class Sports:
    def play(self):
        print("Playing cricket")

class Cricket(Sports):
    def team(self):
        print("The number of players 11")

obj= Cricket()


obj.play()        
obj.team()   





class Device:
    def power_on(self):
        print("The device is now powered on.")

class Phone(Device):
    def __init__(self, brand):
        self.brand = brand
        
    def call(self, number):
        print(f"Making a call to {number} from {self.brand} phone.")
        
    def power(self):
        super().power_on() 
        print(f"{self.brand} phone is powered on.")


obj = Phone("Samsung")
obj.power_on()   
obj.call("123-456-7890")  














