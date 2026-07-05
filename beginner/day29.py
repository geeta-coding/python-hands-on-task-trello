# Generate random int: random.randint(1, 100)
import random

num = random.randint(1, 100)

print(num)


# Generate random float: random.random()
num = random.random()

print(num)


# Choose random element: random.choice(list)
name = ["geeta","ganesh","gauri","siya","rama","lakshman"]

print(random.choice(name))


# Shuffle a list: random.shuffle(list)

numbers = [1, 2, 3, 4, 5]

random.shuffle(numbers)

print(numbers)

# Generate random sample: random.sample(list, k)
numbers = [10, 20, 30, 40, 50]

sample = random.sample(numbers, 3)

print(sample)




# Use math.factorial(), math.gcd(), math.log()
import math

print(math.factorial(10))
print(math.gcd(100,80))
print(math.log(10))

# Use math.sqrt(), math.ceil(), math.floor()
print(math.sqrt(4))
print(math.ceil(12.9))
print(math.floor(12.5))

# Build a dice rolling simulator
dice = random.randint(1, 6)

print("You rolled:", dice)