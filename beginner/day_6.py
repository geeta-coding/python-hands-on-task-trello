
# Write a program to check if a number is positive/negative/zero

number = int(input("enter the number: "))

if number > 0:
    print("you entered  a positive number: {} : ".format(number))
elif number < 0 :
    print("you enterd a negative number : {}".format(number))
else :
    print("you enter the zero number ....")
# Check if a number is even or odd
if number % 2 ==0:
    print("number is even {}".format(number))
else :
    print("odd number {}".format(number))

print()
print("*"*30)

# Build a grade calculator: A(90+), B(80+), C(70+), D(60+), F
marks = int(input("enter the marks : "))
if marks >= 90:
    print("A")
elif marks >= 80:
    print("B")
elif marks >= 70:
    print("c")
elif marks >= 60:
    print("D")
else:
    print("fail....")

print()
print("*"*30)

# Build loan eligibility: age>=21, income>=30000, credit>=700
age = int(input("enter your age: "))
income = int(input("enter the income: "))
credit = int (input("enter the credite: "))

if age >=21:
    if income >= 30000:
        if credit >=700:
            print("you are eligibile for the loan")
        else:
            print("your credits are too low you are not eligible")
    else:
        print("you income is low you are not eligible for loan")
else:
    print("you are now {}".format(age) ,"you are not  eligible")
       
print()
print("*"*30)

# Use nested if-else for complex conditions
password = "admin"
username = "geeta"
name = input("enter the username : ")
passw = input("enter the password : ")

if name == username:
    print("welcome ...now enter the password....")
    if password == passw:
        print("sucessfully log in")
    else :
        print("your password is wrong")
else:
    print("username is wrong")

print()
print("*"*30)
# Use ternary operator: result = 'Pass' if grade >= 60 else 'Fail'
grade = int(input("enter the grade: "))

result = "pass" if grade >=50 else "fail"
print(result)

print()
print("*"*30)
# Build a leap year checker

year = int(input("enter the year for check leap year or not :  "))

if year % 4 == 0 or year % 400 == 0:
    print("{} it is leap year... ".format(year))
else:
    print("{} it is not leap year ...".format(year))

print()
print("*"*30)
# Build a triangle type checker (equilateral/isosceles/scalene)
a = int(input("Enter side 1: "))
b = int(input("Enter side 2: "))
c = int(input("Enter side 3: "))

if a == b == c:
    print("Equilateral Triangle")
elif a == b or b == c or a == c:
    print("Isosceles Triangle")
else:
    print("Scalene Triangle")

print()
print("----------end----------"*5)