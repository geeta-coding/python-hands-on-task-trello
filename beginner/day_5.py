# Take user's name and greet them
user_name = input("ENTER YOUR NAME: ")
print("Wellcome back {}".format(user_name))
print(f"hello {user_name}")


# Take two numbers and print their sum (remember type casting!)
number_1 = input("enter the first number: ")
number_2 = input("enter the second number: ")

print("addition of two number is : ",number_1+number_2)  #  it gives a string value beacuse og input() it is by default string


print("ADDITION: ",int(number_1)+int(number_2))

# Take a birth year and calculate age


from datetime import datetime

birth_date = int(input("Enter Your Bith year : "))
# current_year = int(input("Enter The Current year : "))
current_year = datetime.now().year  # it is dynamically allow

result = current_year - birth_date

print("{} your bith date and now you are completed a {}".format(birth_date,result))


# Handle ValueError when user enters text instead of number
try:
    num = int(input("ente the number for check:  "))
    print("you entered a : ",num)

except ValueError:
    print("enter the number not a string number: ")




# Build a simple tip calculator (bill amount + tip %)

bill = int(input("enter your bill: "))
tip = float(input("enter the tip %: "))

tip_a = (bill*tip)/100
total = bill+tip_a
print("your bill amount is  : {}".format(bill))
print("your tip amount : {}".format(total))

# Build a BMI calculator (weight, height as input)
weight = float(input("enter your weight in (kg) : "))
height = float(input("enter the height in (meter): "))

height = height / 100   # convert cm → meter

bmi = weight / (height * height)
 
print("your BMI is :{:.2f}".format(bmi))



# Use try-except to handle all bad inputs gracefully
try :
    weight = float(input("enter your weight in (kg) : "))
    height = float(input("enter the height in (meter): "))

    height = height / 100   # convert cm → meter

    bmi = weight / (height * height)
 
    print("your BMI is :{:.2f}".format(bmi))
except ValueError:
    print("enter the number not a string or special character")
