# Print the exception hierarchy: BaseException tree


# BaseException
# │
# ├── SystemExit
# ├── KeyboardInterrupt
# ├── GeneratorExit
# │
# └── Exception
#      │
#      ├── ArithmeticError
#      │      ├── ZeroDivisionError
#      │      ├── OverflowError
#      │      └── FloatingPointError
#      │
#      ├── LookupError
#      │      ├── IndexError
#      │      └── KeyError
#      │
#      ├── TypeError
#      ├── ValueError
#      ├── FileNotFoundError
#      ├── AttributeError
#      ├── ImportError
#      ├── RuntimeError
#      ├── OSError
#      └── ...


# Catch specific vs general exceptions
try:
    num = int(input("Enter number: "))
    print(100 / num)

except ValueError:
    print("Please enter numbers only.")

except ZeroDivisionError:
    print("Cannot divide by zero.")




# Use 'as e' to capture error details: except ValueError as e
try:
    age = int("abc")

except ValueError as e:
    print(e)




# Raise exceptions with custom messages: raise ValueError('bad input')
age = -5

if age < 0:
    raise ValueError("Age cannot be negative")




# Create custom exception: class InvalidAgeError(Exception)
age = 15

if age < 18:
    raise InvalidAgeError("Age must be at least 18")




# Add attributes to custom exceptions

try:

    age = 12

    if age < 18:
        raise InvalidAgeError(age)

except InvalidAgeError as e:

    print(e)
    print(e.age)
