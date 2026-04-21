# Write a function greet(name) that prints a greeting

name = input("enter your name : ")

def greet (name):
    print("good morning !! ",name)

greet(name)


# Write a function add(a, b) that returns the sum
num_1 = int(input("enter the number 1 : "))
num_2 = int(input("enter the number 2 : "))

def add(a,b):
    return a+b

print(add(num_1,num_2))


# Use default parameters: greet(name='World')
def greeting(name_1 = "world"):
    print(name_1)


greeting()



# Use *args for variable arguments: sum_all(*args)def 
def sum_all(*args):
    total = 0
    for num in args:
        total += num
    print(total)

sum_all(1,12,12,12,12,4)



# Use **kwargs for keyword arguments
def shop(**item):
    
    total = 0
    for key , values in item.items():
        print(key," = ", values)
        total +=values
    print("totall is ",total)
"""
    Displays key-value details provided as keyword arguments.

    Parameters:
        **kwargs: Variable number of key=value pairs

    Returns:
        None
 """

shop(mobile = 8000, iphone = 80000000,laptop = 90000,tv = 78888)

# Understand local vs global scope
# global
a = 10

def num(a):
    a = 20
    print(a)


num(a)


# Write a function that returns multiple values (tuple)
def marks(m1, m2, m3):
    total = m1 + m2 + m3
    avg = total / 3
    return total, avg

t, a = marks(80, 90, 85)
print("Total =", t)
print("Average =", a)


# Add docstrings to all your functions





