class Cat:
    def name(self):
        print("hi")

class Dog(Cat):
    def name2(self):
        print("hii2")

obj = Dog()
obj.name()  # Output will be "hi"
  

# GREET:


class Grandparent:
    def grandparent_method(self):
        print("This is a grandparent method.")

class Parent(Grandparent):
    def parent_method(self):
        print("This is a parent method.")

class Child(Parent):
    def child_method(self):
        print("This is a child method.")

obj = Child()
obj.grandparent_method()  # Output: This is a grandparent method.
obj.parent_method()       # Output: This is a parent method.
obj.child_method()        # Output: This is a child method.


# OVERRIDING:


class Parent:
 def parent_method(self):
       print("This is a parent method.")

class Child1(Parent):
    pass

class Child2(Parent):
    pass

obj1 = Child1()
obj2 = Child2()

obj1.parent_method()  # Output: This is a parent method.
obj2.parent_method()  # Output: This is a parent method.

