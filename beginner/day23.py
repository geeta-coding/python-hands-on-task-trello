def fabo(n):
    if n==0 or n==1:
        return 1
    else:
        return n *fabo(n-1)

num = int(input("enter the number for the fabonaccia series  : "))

print(f"the factorial of {num} is : {fabo(num)}")

def series (n):
    if n ==0 :
        return 0
    elif n==1:
        return 1
    
    return series(n -1) + series (n-2)

n = int(input("enter the number : "))

for i in range (n):
    print(series(i), end = " ")


def list_sum(lst):
    if len(lst) == 0:
        return 0
    return lst[0] + list_sum(lst[1:])

numbers = [10, 20, 30, 40]

print("Sum =", list_sum(numbers))


def palindrome(s):
    if len(s) <= 1:
        return True

    if s[0] != s[-1]:
        return False

    return palindrome(s[1:-1])

text = input("Enter a string: ")

if palindrome(text):
    print("Palindrome")
else:
    print("Not Palindrome")


def power(x, n):
    if n == 0:
        return 1
    return x * power(x, n - 1)

x = int(input("Enter base: "))
n = int(input("Enter exponent: "))

print("Answer =", power(x, n))

def count_digits(n):
    if n < 10:
        return 1
    return 1 + count_digits(n // 10)

num = int(input("Enter a number: "))

print("Digits =", count_digits(num))

import sys

print(sys.getrecursionlimit())

sys.setrecursionlimit(2000)

print(sys.getrecursionlimit())