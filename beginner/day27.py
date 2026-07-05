# Use enumerate() with custom start index
fruite = ["mango","apple","juice","red-orange","graps","green"]

for index , fruite in enumerate(fruite , start = 1):
    print(index,fruite)




# Use zip() to pair two lists
names = ["geeta","gauri","ganesh","payal","achal"]
marks = [99,80,90,70,80]

for name , mark in zip(names,marks):
    print(name,mark)


# Use zip_longest() for unequal length lists
from itertools import zip_longest
marks = [99,100]
name= ["geeta","raut","amit"]

result= list(zip_longest(name,marks,fillvalue="not available"))

print(result)

# Unzip with zip(*zipped_list)
grades=[("geeta",90),("priya",90),("amit",80)]
name,marks = zip(*grades)
print(name)


# Use itertools.chain() to combine iterables
from itertools import chain,repeat,cycle

list1 = [1,2,3,4]
list2 = [6,3,2,1]
list3 = [12,3,23,2]
combine = list(chain(list1,list2,list3))

print(combine)

# Use itertools.repeat() and itertools.cycle()
for value in repeat("geeta" , 10):
    print(value)

# 
colors = cycle(["Red", "Green", "Blue"])

for i in range(7):
    print(next(colors))
