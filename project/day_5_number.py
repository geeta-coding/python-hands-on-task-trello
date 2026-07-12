import random

print("=" * 40)
print("      GUESS THE NUMBER GAME")
print("=" * 40)

while True:

    # Computer selects a random number
    secret_number = random.randint(1, 100)

    attempts = 0

    print("\nI have selected a number between 1 and 100.")
    print("Can you guess it?")

    while True:

        try:
            guess = int(input("\nEnter your guess: "))
        except ValueError:
            print(" Please enter a valid number.")
            continue

        attempts += 1

        if guess < secret_number:
            print(" Higher!")

        elif guess > secret_number:
            print(" Lower!")

        else:
            print("\n Congratulations!")
            print(f"You guessed the number in {attempts} attempts.")
            break

    choice = input("\nDo you want to play again? (y/n): ").lower()

    if choice != "y":
        print("\nThanks for playing!")
        break