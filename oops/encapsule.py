
class Person:
    def __init__(self, name):
        self.__Name=name

    def name(self):
        return self.__Name

obj=Person("Ragul")
print(obj.name())        
        