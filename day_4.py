# Practice +, -, *, /, //, %, **
num_1 = int(input("enter the number of 1 : "))
num_2 = int(input("enter the number of 2 : "))

def add(a,b):
    return a+b
def sub(a,b):
    return a-b
def mul(a,b):
    return a*b
def divide(a,b):
    return a / b
def floor(a,b):
    return a // b
def mod(a,b):
    return a%b
def expo(a,b):
    return a**b

print("ADDITION IS : ")
print(add(num_1,num_2))
print("SUBTRACTION IS :")
print(sub(num_1,num_2))
print("MULTIPLICATION IS: ")
print(mul(num_1,num_2))
print("DIVIDESTION IS: ")
print(divide(num_1,num_2))
print("FLOOR IS : ")
print(floor(num_1,num_2))
print("MODUAL IS : ")
print(mod(num_1,num_2))
print("EXPONENTION IS : ")
print(expo(num_1,num_2))



# Understand difference between / and //
print("/ it means divid: ",divide(num_1,num_2))

print("// it is floor round-up the value: ",floor(num_1,num_2))



# Use math module: sqrt, ceil, floor, pi
import math 
num = float(input("enter the number"))

print(f"{num} square root is: ",math.sqrt(num))
print(f"{num} ceil is: ",math.ceil(num))
print(f"{num} floor is: ",math.floor(num))
print("the PI values is : ",math.pi)


# Use round() for rounding numbers
print(round(num))
print(round(100.23,2))


# Calculate area of circle, triangle, rectangle

#  AREA OF CIRCLE......
radius  = int(input("enter the radius of circle: "))
area = math.pi*radius*radius
print("Area of CIrcle is : ",area)

# AREA OF TRIANGLE

base = 10
height = 30
area = 0.5 * base * height 
print("Area of Triangle : ",area)

# AREA OF RECTANGLE
lenth = 23
breadth = 14

area = lenth* breadth
print("Area of rectangle : ",area)



# Convert temperature: Celsius to Fahrenheit and back
c = 10
f = (c * 9/5) + 32
print("Fahrenheit",f)


f = 100
c = (f - 32) * 5/9
print("Celsius",c)


# Calculate simple interest and compound interest
p = 12
r = 2
t = 5
si = (p * r * t) / 100
print("SIMPLE INTEREST : ",si)

# Use abs(), pow(), min(), max()

a= -29
print(abs(a))
print(max(12,45,67,78))
print(min("geeta","ajay","shalan","ek"))
print()