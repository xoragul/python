def greet(name):
    return f"Hello, {name}!"


print(greet("World"))  


# RECURSION:

def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n - 1)

print(factorial(5))




#                                        ARGUMENTS

# DEFAULT  ARGUMENTS:


# def greet(name="World"):
#     return f"Hello, {name}!"
# print(greet()) 


# KEYWORD ARGUMENTS:

# def greet(name, message):
#     return f"{message}, {name}!"
# print(greet(name="John", message="Good Morning"))



# POSITION ARGUMENTS:

# def add(a, b):
#     return a + b

# print(add(1, 2)) 



# ARBITARARY ARGUMENTS:


# def add(*args):
#     return sum(args)

# print(add(1, 2, 3))



# LAMBDA EXPRESSIONS:

# add = lambda a, b: a + b
# print(add(5, 3)) 


# MAP:

# nums = [1, 2, 3, 4]
# name = list(map(lambda x: x ** 2, nums))
# print(name)  

