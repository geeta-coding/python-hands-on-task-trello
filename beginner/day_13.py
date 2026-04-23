# Write a lambda to double a number: double = lambda x: x*2
num = int(input("enter the number for double : "))
double = lambda x: x * 2
print(double(num))
#    or

# def double(num):
#     print(num * 2)

# double(num)
#--------------------------------------------------------------------------------



# Use map() to square all numbers in a list
lis = [1,2,3,4,5,6,7,8,6,3,4,5,10]
square = list(map(lambda x: x*x,lis))
print(square)




# Use filter() to get only even numbers
even = list(filter(lambda x : x % 2 == 0,lis))

print(even)




# Use reduce() to calculate product of all numbers
from functools import reduce
num = [1,2,3,4]
result = reduce(lambda x,y : x * y,num) 

print(result)



# Sort a list of tuples by second element using lambda
tup = [("yogesh",90),("sham",10),("geeta",87)]

ans = sorted(tup,key =lambda x: x[0:1] )
print(ans)
print(type(tup))


# Combine map and filter in one line
numbers= [1,2,4,5,6,7,8,9,0,20]
answer = list(
    map(lambda x: x*2,
        filter(lambda x: x %2 ==0,numbers))
)
print(answer)



# Compare lambda vs regular function — when to use which

#=========================================================================================================
# 

# ================================================================================================================

# Use sorted() with key=lambda for custom sorting

name = ["jiya","ram","sham","achal","geeta","eka"]

sort = sorted(name,key= lambda x: x[0])
print(sort)