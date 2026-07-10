# Unpack a list: a, b, c = [1, 2, 3]
numbers =[1,2,3]
# a =numbers[0]
# print(a)  And so on till 3
# insted of we use a unpacking
a,b,c=[1,2,3]
print(a,b,c)



# Use * to capture remaining: a, *rest = [1,2,3,4,5]
num,*ra =[12,2,34,67,7,5]
print(num)
print(*ra) # * use kela jatojevaaaplya mahiti nahi ki kiti values remain ahe

# Use * in function def: def func(*args)


# Use ** in function def: def func(**kwargs)
*start, end = [1, 2, 3, 4]
print(*start,end)

def total(*numbers):
    print(sum(numbers))

total(10, 20)
total(1, 2, 3, 4, 5)

# Unpack dict into function: func(**my_dict)
person = {
    "name": "Geeta",
    "age": 20
}
def show(name, age):
    print(name)
    print(age)

show(**person)

# Merge lists with [*list1, *list2]

num_1 = [12,12,24,23]
num_2 = [1,2,3,4,5]
answer = [*num_1 ,*num_2]
print(answer)


# Merge dicts with {**dict1, **dict2}
dict1 = {
    "name": "Alice"
}
dict2 = {
    "age": 20
}
result = {**dict1, **dict2}

print(result)

# Swap variables: a, b = b, a

print("swapping tow numbers")
number_1 = int(input("enter the number 1: "))
number_2 = int(input("enter the number 2 : "))

number_1 , number_2 = number_2,number_1
print(number_1 , number_2)