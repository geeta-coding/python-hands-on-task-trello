
# Use all() and any() for boolean checks
numbers = [2,4,6, 8,97]
print(all(n%2==0 for n in numbers)) # all() ha only all items true asel trch return kren otherivse no

# if any(user.role == "Admin" for user in users):
#         print("Admin exists")




# Use map() with a function across a list

numbers = [1,2,3,4]
result = map(lambda x: x*x, numbers)

print(list(result))

name = [
    "geeta",
    "rahul",
    "siya"
]
new = list(map(str.upper,name))

print(new)

#  map mnje all elenments la apply hot ekch function for all

# Use filter() to select elements
#   fillter() mde kay ast ki je pn aaply sorting kraych aahe tech use honar mnjetech output hoil 
student = {
    "geeta" : 90,
    "ravi" : 78,
    "yash" :20,
    "achal" :19,
    "gauri" : 89,
    "balu" : 90

}

# passed =list[filter(lambda s:s[student ])
passed = filter(lambda item: item[1] >= 35, student.items())

result = sorted(passed, key=lambda item: item[1])

print(result)



# Use zip() and enumerate() together
foods = ["pizza", "burger", "chips", "potato", "fingerchips"]
prices = [100, 90, 12, 45, 300]

for food, price in zip(foods, prices):
    print(food, price)

print()

for index, food in enumerate(foods, start=1):
    print(index, food)

# Use sorted() with key and reverse


# Use min()/max() with key parameter


# Use sum() with generator expression


# Use isinstance() and type() properly


# Use id() to check object identity


# Use hash() and understand hashable types