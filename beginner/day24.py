# Get ASCII value with ord() and character with chr()
print(ord("a"))
print(ord("b"))
print(ord("c"))
print(ord("d"))


print(chr(12))
print(chr(10))
print(chr(89))
print(chr(87))


# Encode a string to bytes: 'hello'.encode('utf-8')
text = "hello"

encoded = text.encode("utf-8")

print(encoded)
print(type(encoded))


# Decode bytes to string: b'hello'.decode('utf-8')

data = b'hello'

decoded = data.decode("utf-8")

print(decoded)
print(type(decoded))


# Handle UnicodeDecodeError gracefully
data = b'\xff'

try:
    text = data.decode("utf-8")
    print(text)

except UnicodeDecodeError:
    print("Cannot decode the data!")


# Read a file with specific encoding: open(f, encoding='utf-8')
with open("sample.txt", "w", encoding="utf-8") as file:
    file.write("Hello Python")

# Work with emoji in Python strings
print(len("😊"))

# Convert between different encodings
emoji = "😊"

print(emoji.encode("utf-8"))

# Understand the difference between str and bytes
text = "Hello"

utf8 = text.encode("utf-8")
utf16 = text.encode("utf-16")

print(utf8)
print(utf16)