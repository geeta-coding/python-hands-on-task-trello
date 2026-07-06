# Convert decimal to binary: bin(42)
num = 42
print(bin(num))  #0b101010 ha output yeil pn ya mde starting la 0b aahe ha binary nahi aahe he indicate krto ki ha number binary mde dila aahe 
# only 101010 ha number aahe 42 la binary



# Convert decimal to octal: oct(42)
print(oct(num)) # 0o52 yat pn same ch satrting 0o he indicate krto ki ha number ocatal aahe

# Convert decimal to hex: hex(42)
print(hex(num)) #  0x2a satrting 0x he hexadecimal mnun indicate krto

# Convert binary string to int: int('101010', 2)
num_2 = int("101101",2)
print(num_2)

# Use bitwise AND &, OR |, XOR ^, NOT ~
print(10 | 12)
print(10 ^ 6)
print(12 & 23)
print(~10)

# Swap two numbers using XOR without temp variable
a = 10
b = 20

print("Before Swap")
print("a =", a)
print("b =", b)

a = a ^ b
b = a ^ b
a = a ^ b

print("After Swap")
print("a =", a)
print("b =", b)