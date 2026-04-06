# Create a string and use upper(), lower(), title(), strip()
name = "Geeta"
print(name.upper())
print(name.lower())
print(name.title())
print(name.strip())



# Use string slicing: text[0:5], text[::-1] (reverse)

text = "hey hii how are you ?"
print(text[0:23:4]) # 1st where to start 2nd : for where to end and 3rd : use for how many steps you want to drop like that
print(text[0:5])
print(text[::-1]) # reverse a whole text



# Split a sentence into words using split()
state = " India Is MY Country and all Indians are My brother and sister\n i love India .."
print(state.split())
print(state.strip())
print(state.startswith("India"))

# Join a list of words into a sentence using join()
lis = ["I" , "Love ","Coding"]
print(lis)
jo = " ".join(lis)
print(jo)
print(jo.replace("I","WE"))

# Replace words using replace()
print(jo.replace("I","WE"))

# Check contents: startswith(), endswith(), isdigit()
st = "Hello Everyone@123"
print(st.isalnum())
print(st.isdigit())
print(st.startswith("H"))
print(st.endswith("123"))



# Count occurrences with count()
lis_1 = [1,1,2,3,4,5,6,7,7,7,7,1,4,6]
print(st.count("h"))
print(lis_1.count(1))

# Use find() and index() to locate substrings
print(st.find("E"))
print(st.index("y"))


# Format strings with .format() and f-strings
name  = "geeta"
age = 21
print(f"My name is {name} and i am a {age} old ")  # f-string
print("hello my name is  {} and i am {} years old".format(name,age))