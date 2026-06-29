# Invert a dictionary (swap keys and values)
family_memberss = {
    "geeta" : 21,
    "ganesh" :17,
    "gauri" :18,
    "shalan" :38,
    "dnyaneshwar": 40
}

print(family_memberss)
new_family = {value: key for key, value in family_memberss.items()}

print(new_family)

# Merge multiple dictionaries

name = {
    "name" :"geeta"
}
age = {
"age" : 21
}
marks = {
    "grade" : "A++"
}

# answer = name | age | marks
# print(answer)

answer = {}

answer.update(name)
answer.update(age)
answer.update(marks)
print(answer)
# Sort a dictionary by values

marks = {
    "geeta":91,
    "rahul": 80,
    "yanesh": 99
}

sort = dict(
    sorted(marks.items(), key = lambda item : item[1])
)
print(sort)

# Find common keys between two dictionaries
dis = {
    "A" :20,
    "b" : 21,
    "c" : 32,
    "d" :21
}
dis_2 = {
    "A" :20,
    "b" : 21,
    "c" : 32,
    "geeta" : 21

}
common = dis.keys() & dis_2.keys()
print(common)





# Group a list of dicts by a key
students = [

{"name":"Geeta","city":"Pune"},

{"name":"Rahul","city":"Mumbai"},

{"name":"Priya","city":"Pune"}

]

group = {}

for student in students:

    city = student["city"]

    group.setdefault(city, []).append(student)

print(group)

# Access deeply nested dicts safely with .get()
data = {}

python_marks = (
    data.get("student", {})
        .get("marks", {})
        .get("python", "Not Found")
)

print(python_marks)


# Build a simple JSON-like config parser
config = {
    "database": {
        "host": "localhost",
        "port": 3306
    },
    "debug": True
}
host = config.get("database", {}).get("host")

port = config.get("database", {}).get("port")

debug = config.get("debug")

print(host)
print(port)
print(debug)