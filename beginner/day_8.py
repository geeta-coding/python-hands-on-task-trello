# Count down from 10 to 1 using while
num = 10
while num >=1:
    print(num)
    num -= 1


# Build a number guessing game (random number, user guesses)
import random 
secreat_number = random.randint(1,10)
guess = 0

while guess != secreat_number:
     guess = int(input("guess number between 1 to 10:  "))

     if guess < secreat_number:
          print("guess is too low")
     elif guess > secreat_number:
          print("guesss is high")
print("correct you entered: ",guess)

# Keep asking for input until user types 'quit'
text = " "
while text !="q":
     text = input("enter the text: ")
     print()
     print("your respose is : \n",text)



# Calculate factorial using while loop
num= int(input("enter the number for the factorial: "))
fact_1 = 1
while num > 0:
        fact_1 *= num
        num-= 1
print("factorial : ",fact_1)

# Find the first number divisible by both 7 and 13 above 1000
num = 1001
while True:
     if num % 7 == 0 and num % 13 ==0:
          print("answer: ",num)
          break
     num +=1



# Build a simple ATM: deposit/withdraw until 'exit'


balance = 1000

while True:
    choice = input("deposit / withdraw / exit: ")
    
    if choice == "deposit":
        amt = int(input("Enter amount: "))
        balance += amt
    
    elif choice == "withdraw":
        amt = int(input("Enter amount: "))
        if amt <= balance:
            balance -= amt
        else:
            print("Insufficient balance")
    
    elif choice == "exit":
        break
    
    print("Balance:", balance)