# Create a list of 10 student names

student=["geeta","nita","sita","riya","maya","jiva","shiva","mansi","achal","yash"]


# Access elements by index (positive and negative)
print(student[1:])
print(student[1:-7])
print(student[1:10:4]) # it is skips 4 indexes and then print
print(student[::-1])   # reverse 

# Slice lists: first 3, last 3, every 2nd element
print(student[0:10:2])
print(student[0:3])



# Use append(), insert(), extend() to add items
# student.append(23)
print(student)
# student.append(12)
print(student)

# student.extend([23,67,78,])
print(student)

# student.insert(1,54)
print(student)
student.append(["ram","ekta"])
print(student)

# Use remove(), pop(), del to delete items
student.pop()
print(student)
student.remove("geeta")
print(student)



# Sort with sort() and sorted() (ascending and descending)
student.sort()


# Use list comprehension: [x**2 for x in range(10)]

[x**2 for x in range(10)]

# Filter with comprehension: [x for x in nums if x > 5]
nums = [1, 4, 6, 8, 3]
[x for x in nums if x > 5]

# Find min, max, sum, len of a number lis

print(min(student))  # smallest
print(max(student))  # largestgi

print(len(student))  # count

# Check membership with 'in' operator
print(6 in student)   # false
print("ramin"in student)  