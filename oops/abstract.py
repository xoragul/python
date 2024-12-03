from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self): 
        pass

    @abstractmethod
    def perimeter(self): 
        pass

class Rectangle(Shape):
    
    def __init__(self, width, height):
        self.width, self.height = width, height
        
    def area(self): 
        return self.width * self.height
        
    def perimeter(self): 
        return 2 * (self.width + self.height)

# Create a Rectangle object
w = Rectangle(2, 3)

# Print the area and perimeter
print("Area:", w.area())
print("Perimeter:", w.perimeter())

