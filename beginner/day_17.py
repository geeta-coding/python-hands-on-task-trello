#   linear search by using python
# ya linear search mde jar data sorted nsel tri chalto karn linear search prtek index la jaun value check krto
# aani ya mde worst case ha aahe ki ya mde time complexity pn jast aahe


def linear(arr,search):
    for i in range(len(arr)):
        if arr[i]==search:
            return i
    return -1
        

arr = [12,5,7,8,12,89]
search = int(input("enter the number for search: "))
result = linear(arr,search)

if result != -1:
    print("key find ",result)
else:
    print("not found")


# implemented a binary search ya mde aapn two parats kro mnje fist mid find krto aani mg compare krto mid aani search value 
 # jr mid vale > asel seach value peksha tr right sidela search krto aani jr < asel tr left sidela la search krto 
 # ha approch best case mde aahe karn time complexity kmi aahe
def binary(arr, search):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2

        if arr[mid] == search:
            return mid

        elif arr[mid] < search:
            low = mid + 1

        else:
            high = mid - 1

    return -1


arr = [2, 5, 8, 12, 16, 20, 25]

search = int(input("Enter number to search: "))

result = binary(arr, search)

if result != -1:
    print("Element found at index:", result)
else:
    print("Element not found")


#  implemented bubble sort

arr = [5, 3, 8, 1]

n = len(arr)

for i in range(n):

    for j in range(0, n-i-1):

        if arr[j] > arr[j+1]:

            arr[j], arr[j+1] = arr[j+1], arr[j]

print(arr)

# selection sort ya sorting method mde smalllest value select krt 
def selection_sort(arr):

    n = len(arr)   # it output 5 yeil

    i = 0  # assume that first no. is 0 

    while i < n:  # jo praunt n mnje 5 ha 0 peksha kmi hot n y to vr run hoil 

        min_index = i   # aata minimum value la set kel aahe 0th index

        j = i + 1    #aata check krayla j+1 sangitl aahe mnjech index 1 aahe j cha ani i cha 0

        while j < n: # 1<5 aahe ka check kren aahe tr khali yeil as te 2<5 3<5 4<5 it praynt chalen 

            if arr[j] < arr[min_index]:   # aata ite khara logic aahe mnje check kren 1 st index < 0 mnjech 64<25 aahe tr
                min_index = j # minimum no ha j la jail 

            j += 1 # ite value ekn vaden

        arr[i], arr[min_index] = arr[min_index], arr[i]

        i += 1

    return arr


arr = [64, 25, 12, 22, 11]

print("Original Array:", arr)

selection_sort(arr)

print("Sorted Array:", arr)

arr = []
n = int(input("enter the no : "))


for i in range (n):
    value = int(input("enter the value: "))
    arr.append(value)


print("list is : ",arr)


def insertion_sort(arr):

    # Traverse from index 1 to end
    for i in range(1, len(arr)):

        key = arr[i]      # Current element
        j = i - 1         # Previous index

        # Shift elements greater than key
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j = j - 1

        # Place key at correct position
        arr[j + 1] = key

    return arr


# User Input
arr = []

n = int(input("Enter number of elements: "))

for i in range(n):
    value = int(input("Enter element: "))
    arr.append(value)

print("Original List:", arr)

sorted_arr = insertion_sort(arr)

print("Sorted List:", sorted_arr)




def quick_sort(arr):

    # Base condition
    if len(arr) <= 1:
        return arr

    # Choose pivot
    pivot = arr[0]

    # Elements smaller than pivot
    left = []

    # Elements greater than pivot
    right = []

    # Equal elements
    middle = []

    for num in arr:
        if num < pivot:
            left.append(num)

        elif num > pivot:
            right.append(num)

        else:
            middle.append(num)

    # Recursive sorting
    return quick_sort(left) + middle + quick_sort(right)


# User Input
arr = []

n = int(input("Enter number of elements: "))

for i in range(n):
    value = int(input("Enter element: "))
    arr.append(value)

print("Original List:", arr)

sorted_arr = quick_sort(arr)

print("Sorted List:", sorted_arr)

print("\n sorting using prefefined sorted() in python .....")
arr = [12,5,2,90,1,76,45,67]

print(sorted(arr))