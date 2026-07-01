# List comprehension with condition: [x for x in range(100) if x%3==0]
numbers = [x for x in range(100) if x %3==0]
print(numbers)

# Nested list comprehension: flatten 2D list
matrix = [
    [1,2,3,4],
    [12,67,6,5],
    [12,78,5,34]
]

flat = [item for row in matrix for item in row]
print(flat)

# Dict comprehension: {k:v for k,v in zip(keys,vals)}

key = ["name","age","city"]
value= ["geeta",21,"pune"]


student = {
    k:v for k,v in zip(key,value)
}

print(student)
# Set comprehension: unique lengths of words
fruit = ["apple","banan","cherry","mango","icecream"]
lenth = {
    len(fruit) for fruit in fruit
}

print(lenth)

# Comprehension with if-else: ['even' if x%2==0 else 'odd' for x in nums]
if_or_even = [12,3,56,78,5,54]
result = ["even" if x % 2 == 0 else "odd" for x in if_or_even]

print(result)

# Nested dict comprehension
table = {i: {j: i * j for j in range(1, 6)} for i in range(1, 6)}

print(table)

# Generator expression for memory efficiency

gen = (x * x for x in range(10))

print(gen)

# # Compare comprehension vs for-loop performance with timeit
for num in gen:
    print(num)