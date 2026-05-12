# Check if a string is a palindrome
name = input("enter the string : ")
print("your string name is  : ",name)


if name == name[::-1]:
    print(f"{name} is palindrom")

else:
    print("it is not a palindrom number")





# Count vowels and consonants in a string
vowels = 0
constant = 0
character = input("enter the string : ")
print("the character is : ",character)

for ch in character:
      if ch.isalpha():
       if ch in "aeiouAEIOU":
        # print("it is vowel ")
        vowels +=1
       else:
        # print("constant")
        constant =+ 1

print("total vowels are : ",vowels)
print("\n constant is : ",constant)



# Reverse words in a sentence (not characters)
sentance = input("enter the sentance : ")
word = sentance.split()
reversed_sentance = " ".join(word[::-1])

print(reversed_sentance)



# Check if two strings are anagrams

string = input("enter the string value : ")
string_2 = input("enter the secount anagrous : ")

if sorted(string) == sorted(string_2):
   print("anagram string")
else:
   print("it is not a anagram")


# Remove duplicate characters from a string

sentance = input("enter the sentance for a removing a duplication : ")
output = ""

for ch in sentance:
   if ch not in output:
      output +=ch
print("after removing : ",output)


# Find the most frequent character in a string
char = input("enter the character for checking : ")

max_ch = ''
max_count = 0

for ch in char:
   count = char.count(ch)

   if count >max_count:
      max_count=count
      max_ch = ch

print("Frequency:", max_count)
print("Most frequent character is:", max_ch)

s = input("Enter snake_case string: ")

words = s.split("_")

camel = words[0]

for word in words[1:]:
    camel += word.capitalize()

print("camelCase:", camel)
   



# Validate an email format 
import re

email = input("Enter email: ")

pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'

if re.match(pattern, email):
    print("Valid Email")
else:
    print("Invalid Email")