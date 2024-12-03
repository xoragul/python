# class Person():
#     def __init__(self,a):
#         self.A=a

# obj=Person("dog")

# print(obj.A)  




class Rich():
    def __init__(self,brand,model):

        self.Brand=brand
        self.Model=model

obj=Rich("BMW","120")

print(obj.Brand)
print(obj.Model)





# class Person():
#     def __init__(self,letter):

#         self.Letter=letter

# obj=Person("Hello!")

# print(obj.Letter)



# class Student():
#     def __init__(self,i):
        
#         self.A=i

# obj=Student("i am a student")        

# print(obj.A)



# class Person():
#     def __init__(self,age):

#         self.set_age=age

# obj=Person(20)

# print(obj.set_age)
        




# class Book():
#     def __init__(self,tittle,author):

#         self.Tittle=tittle
#         self.Author=author

# obj=Book("Grandmaster","Ragul")

# print(obj.Tittle)
# print(obj.Author)



class Rectangle():
    def __init__(self,width,height):
        self.Width, self.Height = width ,height

        
    def area (self):
        return self.Width*self.Height

    def perimeter(self):
        return 2*(self.Width + self.Height)   
    

obj=Rectangle(2,3)

print(obj.area())
print(obj.perimeter())



class Circle():
     def __init__(self,radius):
         
         self.Radius = radius

     def area(self):
         return 3.14 * self.Radius **2
            
     
obj=Circle(5)

print(obj.area())






class Player():
    def __init__(self,cricket):
        self.Cricket=cricket

        
obj=Player("RAGUL")

print(obj.Cricket)



class Animals():
    def __init__(self,noice):
        self.NOICE=noice

obj=Animals("ANIMAL MAKE A SOUND")

print(obj.NOICE)













