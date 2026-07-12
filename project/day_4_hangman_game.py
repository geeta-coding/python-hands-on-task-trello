
# Store a list of 50+ words by category
import random
import random

# ----------------------------
# WORDS (50+)
# ----------------------------

WORDS = {
    "Animals": [
        "elephant", "tiger", "lion", "zebra", "giraffe",
        "rabbit", "monkey", "dolphin", "camel", "penguin"
    ],

    "Fruits": [
        "apple", "banana", "orange", "mango", "papaya",
        "grapes", "pear", "kiwi", "pineapple", "watermelon"
    ],

    "Countries": [
        "india", "canada", "brazil", "france", "germany",
        "italy", "nepal", "japan", "mexico", "norway"
    ],

    "Technology": [
        "python", "keyboard", "monitor", "database",
        "network", "internet", "compiler",
        "software", "hardware", "algorithm"
    ],

    "Sports": [
               
        "cricket", "football", "tennis", "hockey",
        "boxing", "cycling", "archery",
        "kabaddi", "volleyball", "badminton"
    ]
}


# ----------------------------
# HANGMAN STAGES
# ----------------------------

HANGMAN = [

"""
 +---+
 |   |
     |
     |
     |
     |
=========
""",

"""
 +---+
 |   |
 O   |
     |
     |
     |
=========
""",

"""
 +---+
 |   |
 O   |
 |   |
     |
     |
=========
""",

"""
 +---+
 |   |
 O   |
/|   |
     |
     |
=========
""",

"""
 +---+
 |   |
 O   |
/|\\  |
     |
     |
=========
""",

"""
 +---+
 |   |
 O   |
/|\\  |
/    |
     |
=========
""",

"""
 +---+
 |   |
 O   |
/|\\  |
/ \\  |
     |
=========
"""
]


wins = 0
losses = 0


# ----------------------------
# FUNCTIONS
# ----------------------------

def choose_word():
    category = random.choice(list(WORDS.keys()))
    word = random.choice(WORDS[category])
    return category, word


def display_word(word, guessed):
    display = []

    for letter in word:
        if letter in guessed:
            display.append(letter)
        else:
            display.append("_")

    return " ".join(display)


def play_game():

    category, word = choose_word()

    guessed_letters = set()

    wrong_guesses = 0

    print("\n========================")
    print("      HANGMAN GAME")
    print("========================")
    print("Category:", category)

    while True:

        print(HANGMAN[wrong_guesses])

        print("Word :", display_word(word, guessed_letters))

        print("Guessed :", " ".join(sorted(guessed_letters)))

        print(f"Remaining Chances : {6 - wrong_guesses}")

        guess = input("\nGuess a letter : ").lower().strip()

        # ---------------- Validation ----------------

        if len(guess) != 1:
            print("Enter ONLY one letter.")
            continue

        if not guess.isalpha():
            print("Letters only.")
            continue

        if guess in guessed_letters:
            print("Already guessed.")
            continue

        guessed_letters.add(guess)

        # ---------------- Correct ----------------

        if guess in word:
            print("Correct!")

        else:
            wrong_guesses += 1
            print("Wrong!")

        # ---------------- Win ----------------

        if all(letter in guessed_letters for letter in word):
            print("\nCongratulations!")
            print("You guessed:", word)
            return True

        # ---------------- Lose ----------------

        if wrong_guesses == 6:
            print(HANGMAN[6])
            print("\nGame Over")
            print("Word was:", word)
            return False


# ----------------------------
# MAIN LOOP
# ----------------------------

while True:

    if play_game():
        wins += 1
    else:
        losses += 1

    print("\nScore")
    print("Wins   :", wins)
    print("Losses :", losses)

    again = input("\nPlay Again? (y/n): ").lower()

    if again != "y":
        break


print("\nThanks for playing!")