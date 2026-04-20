#  dictionary method

# writing a simple dict
student = {
    "name" : "geeta",
    "age" : 21,
    "marks": 99
}
print(student)

#  access by the key names

print(student["name"])

# create a dict using the keyword

# emp = dict({
#     "name": "ram",
#     "age": 30
# })

# print(emp)
#  tasks =========================================================================================
# Create a phone book dict: {name: number}
phone_number = {
    "geeta" : 70298298,
    "balu": 904987837,
    "ganesh":96787,
    "amol":9078676,
    "sonu":89890,
    "renuka":220922,
    "kanya":289823,
    "gauri":908837,
    "swati":9021912,
    "ritesh":897876
}
print(phone_number)

print(phone_number.get("geeta"))
print(phone_number.get("balu"))

for key , value in phone_number.items():
    print(key,value)

#  searching number
search = input("enter your name: ")
for key , value in phone_number.items():
    if search == key:
        print("number : ",value)
        break
else:
    print("no match try again")



# Access values with [] and .get() (understand the difference)
# print(phone_number["sita"])  # keyerror yenar it karn sita name chi key aapn declare nahi keli mnun
print(phone_number.get("sita")) # ite error show nahi honar ite by default la jaun (none) yeil...




# Add, update, and delete entries
phone_number["geeta"] = 7057898 
print(phone_number)
del phone_number["geeta"] # ite delete hoil
print(phone_number)



# Loop through keys, values, and items
search = input("enter your name: ")
for key , value in phone_number.items():
    if search == key:
        print("number : ",value)
        break
else:
    print("no match try again")

print(len(phone_number)) 
print(phone_number.values()) 
print(phone_number.keys()) #fkt keys provide krty
print(phone_number.items()) # all key value pairs dete
phone_number.popitem() #lastch delete krty
print(phone_number)

# Use dict comprehension: {x: x**2 for x in range(5)}
for i in phone_number:
    print(phone_number[i])

home_phone_numbers = phone_number.copy()
print(home_phone_numbers)


# Build a word frequency counter from a sentence
sentence = input("enter the sentance for checking a count of the word: ").lower()
word = sentence.split()

word_count = {}

for i in word:
    if i in word_count:
        word_count[i] += 1
    else:
        word_count[i] = 1

print("word frequency is : ")
for i , j in word_count.items():
    print(i," : ",j)

# Create nested dicts: students with name, age, grades
student_1 = {
    "101" : {"name": "geeta","age":21,"marks" :99
    },
    "102" : {"name": "ravi","age":29,"marks" :91},
    "103" : {"name": "isha","age":21,"marks" :79},
    
    "104" : {"name": "raya","age":28,"marks" :98},
    "105" : {"name": "sita","age":21,"marks" :89},

}
print(student_1)
print(student_1.get("hjjj"))

# Merge two dicts using | operator or .update()
phone_number.update({'balu':70286767})
phone_number.update({'swati':90213888})
print(phone_number)


# Use setdefault() and defaultdict
a = phone_number.setdefault('color','white')
print(a)