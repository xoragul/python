print("hello")

a=5
b=10
print(a+b)


a="ragul"
print(a)


a=100
print(a)


x = 5
y = "vijay"
print (type(x))
print(y)


x = "John"
print(x)
x = 'John'
print(x)

a=2j
x = 5
y = "John"
z=3.509

print(type(a))
print(type(x))
print(type(y))
print(type(z))



x = ["apple", "banana", "cherry"]
print(x)
print (type(x))


x = ("apple", "banana", "cherry")
print(x)
print (type(x))



a=5
if a>5:
    print("grater is a")
elif a<5:
    print("greater than of 5")   
else :
    print("equal")



a=5
if a>0:
    print("possitive ")
else :
    print("negative")    



a = int(input("enter the age: ") )
if a>=18:
    print("eligible for vote")
else:
    print("not eligible")


a =int (input("enter the mark: "))
if a>=90:
    print("Grade : A ") 

elif a>=80:
    print("Grade : B ")

elif a>=70:
    print("Grade : C ")

elif a>=60:
    print("Grade : D ")   

elif a>=40 and a<60:
    print("Grade : E ")

else:
    print("Fail")


a=int(input ("enter the number : "))

if a>0:
    if a%2==0:
        print("number is positive and even")
    else:
        print("number is positive and odd")    

else:
    print("number is negative")     



a=int(input ("Enter the year : ")) 

if a%4==0:
    print(" It is a leap year")
else :
    print("Not leap year")



indexing = "hello"
print(indexing[1])


slicing = "ragul"
print(slicing[0:4])

modify="kajini"
modify1= modify.replace("k","r")
print(modify1)

concatenate="hello"
concatenate1="world"
concatenate3= concatenate+""+concatenate1
print(concatenate3)


name = "Alice"
age = 25
formatted= f"{name} is {age} years old."
print(formatted)


escape = "He said,\"Hello\""
print(escape)


s= "Hello,World,Python"
split1= s.split(",") 
print(split1)


a = "Hello, World!"
print(len(a)) 
