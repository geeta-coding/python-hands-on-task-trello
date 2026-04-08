# nam , age , city
print("my name is geeta raut , i am 21 years old i am from pune")

# f-string uses
name = "geeta"
print(f"my name is {name}")

# escape characters

print("my name is geeta \n i am 21 years old \037[92m" \
"  okkkk",end=".......")

msg = """  
hello everyone nice to meet you this is a python day 1 course here is a multiline msg from a python to you
"""
print (msg)

# without using external libraries
name = "Geeta"

print(f"{name:*
         <30}")  # Left
print(f"{name:*>10}")  # Right
print(f"{name:*^50}")  # Center