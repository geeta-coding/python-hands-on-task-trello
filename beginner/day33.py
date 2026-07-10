# Demonstrate local scope inside a function
def greet_1 ():
    print("hello geeta ")

greet_1()


# Demonstrate global scope
name = "geeta"

def greet():
    print("welcome to google company", name)


greet()


# Use 'global' keyword to modify global variable inside function
def change_name():
    global name
    name ="gauri"
    print("updated name by using a global keyword",name)

change_name()


# Understand nested function scope (enclosing)
def outer():
    name = "geeta"

    def inner():
        print(name)

    inner()

outer()


# Use 'nonlocal' keyword for enclosing scope
def out():
    count =0
    def inn():
        nonlocal count
        count += 1
        print(count)

    inn()

out()
out()


# Demonstrate variable shadowing

name = "Global"

def show():
    name = "Local"
    print(name)

show()
print(name)

# Understand why mutable defaults are dangerous
def add_item(item, my_list=None):

    if my_list is None:
        my_list = []

    my_list.append(item)

    return my_list

print(add_item(1))
print(add_item(2))
print(add_item(3))


# Practice: predict output of 5 scope-related code snippets
x = 5

def test_sample():
    x = 10
    print(x)

test_sample()
print(x)

#  out is a 10 and then 5
x = 5

def test():
    print(x)

test() 

# answer is 5
count = 0

def add():
    global count
    count += 1

add()
add()

print(count)
# 2 answer
def outer_1():

    x = 100

    def inner():
        print(x)

    inner()

outer_1()

#  answer 100
def outer_2():

    x = 10

    def inner():
        nonlocal x
        x += 2

    inner()

    print(x)

outer_2()
# answer 12