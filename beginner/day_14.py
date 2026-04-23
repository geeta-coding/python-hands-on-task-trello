#  ======================================================================================================
# exception handling programs for the practice
try:
    num = int(input("enter the number for the division : "))
    result = 10/num
    

except ZeroDivisionError:
    print("incoorect values")

else:
    print("result is  : ",num,result)


try :
   age  =int(input("enter the age: ")) 

except ValueError:
    print("value error")

else:
    print("yout age is ",age)
#     Catch ZeroDivisionError
try:
    x = 10 / 0
except ZeroDivisionError:
    print("Cannot divide by zero")

# Catch ValueError for bad type conversion

try:
    num = int("abc")
except ValueError:
    print("Invalid number input")


# Catch FileNotFoundError when opening missing files
try:
    f = open("data.txt")
except FileNotFoundError:
    print("File does not exist")

# Use multiple except blocks for different errors

try:
    num = int(input("Enter number: "))
    result = 10 / num
except ValueError:
    print("Enter valid number")
except ZeroDivisionError:
    print("Cannot divide by zero")

# Use else block (runs if NO exception)

try:
    num = int("10")
except ValueError:
    print("Error occurred")
else:
    print("Success! Number is:", num)

# Use finally block (runs ALWAYS)
try:
    f = open("data.txt")
except FileNotFoundError:
    print("File missing")
finally:
    print("This always runs")

# Use 'raise' to raise your own exceptions
def withdraw(balance, amount):
    if amount > balance:
        raise Exception("Insufficient balance")
    return balance - amount

withdraw(1000, 2000)


# Create a custom exception class


# Use try-except in a loop for retry logic
