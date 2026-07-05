# Use Counter to count element frequencies
from collections import Counter

fruits = ["apple","banana","cherry","mango","geeta","raut","ganesh","ganesh","gauri","geeta"]

count=  Counter(fruits)
print(count)





# Find top N most common elements with Counter.most_common()

numbers = [1,2,2,2,3,3,3,4,4,4,1]
count_1 = Counter(numbers)
print(count_1.most_common(3))


# Use defaultdict to avoid KeyError
from collections import defaultdict
d = defaultdict(int)

d["apple"] += 1

print(d)


# Use namedtuple for readable data records
from collections import namedtuple
student=  namedtuple("student",["name","age","marks"])

s = student("geeta",20,99)
print(s.name)

# Use deque for efficient append/pop from both ends
from collections import deque

dq = deque()

dq.append(10)
dq.append(15)
dq.append(25)
print(dq)

dq.popleft()
print(dq)


# Use OrderedDict when insertion order matters

from collections import OrderedDict

d = OrderedDict()
d["A"]=1
d["B"]=2
d["C"]=3

print(d)


# Use ChainMap to merge dictionaries
from collections import ChainMap

d1 = {"a": 1, "b": 2}
d2 = {"b": 20, "c": 30}

merged = ChainMap(d1, d2)

print(merged["a"])
print(merged["b"])
print(merged["c"])


# Compare performance: list vs deque for appendleft
lst = []

lst.insert(0, 10)
print(lst)

from collections import deque

dq = deque()

dq.appendleft(10)
print(dq)