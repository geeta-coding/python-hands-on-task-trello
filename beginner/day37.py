# Understand what None is (it's NOT 0 or False or '')
print(None)

print(None == 0)
print(None == False)
print(None == "")
# Check for None with 'is None' (not == None)
x = None

if x is None:
    print("no value is there")


# List all falsy values: None, 0, '', [], {}, set(), False
values = [False, None, 0, "", [], {}, set()]

for value in values:
    if value:
        print("True")
    else:
        print("False")

# Understand truthy: non-zero, non-empty are True
print(bool(100))
print(bool("Hello"))
print(bool([1,2]))

# Use 'if x' vs 'if x is not None' (know the difference)

age = 0

if age:
    print("your age is active")
else:
    print("you are die....")

age = 0

if age is not None:
    print("Age exists")


# Default function returns: what happens without return?
def add(a,b):
     c = a+b
    #  return c

print(add(12,2))


# Handle optional function parameters with None default



# Debug a 'NoneType' error in practice code
def get_name():
    # print("Geeta") 
    return "geeta"

name = get_name()

print(name.upper())