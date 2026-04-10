# rint numbers 1 to 100 using range()
for i in range(1,100):
    print(i)

# Print only even numbers from 1-50
for i in range (1,51):
    if i % 2 ==0:
        print(i)


# Calculate sum of all numbers from 1-1000
total = 0
for i in range (1,1001):
    total += i
print(total)


# Use enumerate() to loop with index
lis = ["geeta",21,26,"ekta"]

for i, valu in enumerate(lis):
    print(i,valu) 
print()

# Use zip() to loop over two lists simultaneously
name= ["geeta","seeta","neeta","ekta"]
marks = [99,90,92,100]

for name , marks in zip(name,marks):
    print(name,marks)


# Build a multiplication table (1-10) using nested loops

for i in range(1,11):
    for j in range(1,11):
        print(i*j,end = "  ")
    print()

# Print a right triangle pattern with *
for i in range(1,6):
    print(i*"*" )


# Use break and continue statement
for i in range (1,10):
     if  i ==5 :
         break
     print(i)

for i in range (1,10):
    if i ==4:
        continue
    print(i)


# Build FizzBuzz (1-100): Fizz for 3, Buzz for 5, FizzBuzz for both
for i in range (1,100):
    if i % 30 ==0 :
        print(i,"fizz")
    elif i % 5 ==0 :
        print(i,"buzz")
    elif i % 3 ==0 and i%5 ==0 :
        print(i,"fizz-buzz")
    else:
        print("----")


