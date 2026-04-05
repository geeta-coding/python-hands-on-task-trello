# Create variables: int, float, str, bool

age = 21
marks = 90.99
name = "geeta"
academic = True

print(f"my name is {name} and currently i am {age} years old \nrecently i was topped a python examination with {marks} percentage")



# Use type() to check each variable's type
print (type(age),type(marks),type(name),type(academic))

# Convert string '42' to int
str = '42'
print(type(str))
str = int(str)
print(type(str))

# Convert int 42 to float
str = float(str)
print(type(str))

# Convert float 3.14 to int (notice truncation)
float_to_int = int(3.14)
print(float_to_int)


# Use isinstance() to verify types
name_1 = "geeta"
print(isinstance(10, int))

# Practice multiple assignment: a, b, c = 1, 2, 3
a = b = c = 200
print(a,b,c) # 200 for each number
name = username= "ram"
print (name , username)


# Swap two variables without temp variable

a = 20 
b =30
a,b = b,a
print (a,b)