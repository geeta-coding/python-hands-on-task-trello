# Create a tuple and try to modify it (see the error)
tup = (12,34,45,6,67,8,8,8,9,988)
# print(type(tup))
print(tup.count(6))
print(len(tup))
print(tup[0:2])
# tup[0] = 12
print(tup)


# Use tuple unpacking: a, b, c = (1, 2, 3)
a,b,c = (1,2,3)
print(a)

# Use tuples as dictionary keys (lists can't do this!)
d = {
    (1, 2,5): "geeta",
    (3, 4,6): "good girl"
}

print(d[(1, 2,5)])
print(d[(3, 4,6)])




# Create a set and add duplicate values (notice they disappear)
set_sample = {12,2,2,2,45,56,67,90,45}
print(type(set_sample))
s= {12}
print(type(s))

print(set_sample)


# Use set operations: union |, intersection &, difference -
a = {1, 2, 3}
b = {3, 4, 5}

print(a | b)  
print(a & b)  
print(a - b)  


# Remove duplicates from a list using set()
list_sample = [12,2,3,4,55,55,2,3,56,55,12,12]
unique = list(set(list_sample))
print(list_sample)
print("removed a duplicates : ",unique)

# Use frozenset for immutable sets
ses = frozenset([12,45,65])
# ses.add(12) 
print(ses)


# Compare performance: list vs set for 'in' operator
lis = [1,5,7,0,2,3,5,7]
st = {1,5,3,3,7,6,4}
print(5 in lis)
print(3 in st)
