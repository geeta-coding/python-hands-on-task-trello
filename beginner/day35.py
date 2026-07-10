# Ternary: result = 'yes' if condition else 'no'

grade = 40
result = "pass" if grade >=40 else "fail"
print(result)

# Nested ternary (and why to avoid it)
age = 15

result = (
    "Child" if age < 13
    else "Teen" if age < 18
    else "Adult"
)
print(result)


# Walrus operator: if (n := len(data)) > 10: print(n)
data = [1, 2, 3]

if (n := len(data)) > 2:
    print(n)


# Use walrus in while loops: while (line := input()) != 'quit'
line = input()

while line != "quit":
    print(line)
    line = input()


# # Use walrus in list comprehensions
# words = ["cat", "elephant", "dog", "python"]

# result = []

# for word in words:
#     length = len(word)
#     if length > 3:
#         result.append(length)

# print(result)
words = ["cat", "elephant", "dog", "python"]

result = [length for word in words if (length := len(word)) > 3]

print(result)


# Chain comparisons: 1 < x < 10
x = 5

if 1 < x < 10:
    print("Valid")


# Use or for default values: name = input() or 'Anonymous'
name = input("Name: ") or "Anonymous"

print(name)


# Multiple assignment: a = b = c = 0

a=b=c=1
x =y =z =0
print(a,b,c)
print(x,y,z)