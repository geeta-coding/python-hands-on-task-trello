# ==========================================
# Python Sets - Common Operations
# ==========================================

# Sample lists
list1 = [1, 2, 2, 3, 4, 5]
list2 = [4, 5, 5, 6, 7]

# ------------------------------------------
# 1. Find unique items in a list
# ------------------------------------------
unique_items = set(list1)
print("Unique items:", unique_items)

# ------------------------------------------
# 2. Find common elements (Intersection)
# ------------------------------------------
common = set(list1).intersection(set(list2))
print("Common elements:", common)

# ------------------------------------------
# 3. Find elements in list1 but not in list2
#    (Difference)
# ------------------------------------------
difference = set(list1).difference(set(list2))
print("Only in list1:", difference)

# ------------------------------------------
# 4. Find all unique elements from both lists
#    (Union)
# ------------------------------------------
union = set(list1).union(set(list2))
print("Union:", union)

# ------------------------------------------
# 5. Find elements in either list but not both
#    (Symmetric Difference)
# ------------------------------------------
sym_diff = set(list1).symmetric_difference(set(list2))
print("Symmetric Difference:", sym_diff)

# ------------------------------------------
# 6. Fast membership testing using a set
# ------------------------------------------
numbers = set(range(100000))

if 99999 in numbers:
    print("99999 found in the set.")

# ------------------------------------------
# 7. Remove duplicates while preserving order
# ------------------------------------------
numbers = [3, 1, 2, 3, 4, 2, 5, 1]

seen = set()
unique_ordered = []

for num in numbers:
    if num not in seen:
        seen.add(num)
        unique_ordered.append(num)

print("Without duplicates (order preserved):", unique_ordered)

# ------------------------------------------
# 8. Simple Spell Checker using a set
# ------------------------------------------
dictionary = {
    "python",
    "programming",
    "computer",
    "keyboard",
    "mouse",
    "screen",
    "developer"
}

word = input("Enter a word: ").lower()

if word in dictionary:
    print("✅ Correct spelling!")
else:
    print("❌ Word not found in dictionary.")