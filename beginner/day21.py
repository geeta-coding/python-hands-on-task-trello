lis = [12,2,6,7,34,56,7,8,9,12]

print(lis)

# Reverse a list using slicing [::-1]
print(lis[::-1])


# Get every nth element from a list
print(lis[::2])
print(lis[1:2:7])


# Rotate a list left by k positions
k = 2
rotate = lis[k:] + lis[:k]
print(rotate)


# Flatten a nested list [[1,2],[3,4]] -> [1,2,3,4]
flat = []

for sublist in nested:
    for item in sublist:
        flat.append(item)

print(flat)


# Remove duplicates while preserving order
nums = [1,2,2,3,4,3,5]

result = []

for x in nums:
    if x not in result:
        result.append(x)

print(result)

# Interleave two lists [1,2,3] + [a,b,c] -> [1,a,2,b,3,c]
a = [1,2,3]
b = ['a','b','c']
result = []

for x, y in zip(a, b):
    result.append(x)
    result.append(y)

print(result)

# Chunk a list into groups of n
chunks = []

for i in range(0, len(nums), n):
    chunks.append(nums[i:i+n])

print(chunks)