import random
# it aapn random access krnya sathi ite impert kel aahe

EMOJIS = {
    "rock": "🪨",
    "paper": "📄",
    "scissors": "✂️",
    "lizard": "🦎",
    "spock": "🖖"
}


def get_mode():
    # it declare kel aahe tumi choice kra tumi simple khelnar ki hard 
    while True:  # jo pryant true aahe to vr chalva looop
        mode = input("Choose game mode:\n1. Classic (Rock, Paper, Scissors)\n2. Extended (Rock, Paper, Scissors, Lizard, Spock)\nEnter 1 or 2: ")
# jar user ne 1 type kel te he kra
        if mode == "1":
            choices = ["rock", "paper", "scissors"]
            wins = {
                "rock": ["scissors"],
                "paper": ["rock"],
                "scissors": ["paper"]
            }
            return choices, wins
# jar user ne 2 kel atr he kra
        elif mode == "2":
            choices = ["rock", "paper", "scissors", "lizard", "spock"]
            wins = {
                "rock": ["scissors", "lizard"],
                "paper": ["rock", "spock"],
                "scissors": ["paper", "lizard"],
                "lizard": ["paper", "spock"],
                "spock": ["rock", "scissors"]
            }
            return choices, wins

        else:
            print("Invalid choice.\n")


def get_best_of():
    while True:
        try:
            rounds = int(input("\nPlay best of (3 / 5 / 7): "))
            if rounds in [3, 5, 7]:
                return rounds
            print("Choose 3, 5, or 7.")
        except ValueError:
            print("Enter a valid number.")


def get_player_choice(choices):
    while True:
        choice = input(f"\nChoose {', '.join(choices)}: ").lower()

        if choice in choices:
            return choice

        print("Invalid choice.")


def determine_winner(player, computer, wins):
    if player == computer:
        return "tie"

    if computer in wins[player]:
        return "player"

    return "computer"


def main():
    print("=" * 40)
    print("🎮 Rock Paper Scissors")
    print("=" * 40)

    choices, wins = get_mode()
    best_of = get_best_of()

    wins_needed = best_of // 2 + 1

    player_score = 0
    computer_score = 0
    total_rounds = 0

    while player_score < wins_needed and computer_score < wins_needed:
        player = get_player_choice(choices)
        computer = random.choice(choices)

        print(f"\nYou:      {EMOJIS[player]} {player.title()}")
        print(f"Computer: {EMOJIS[computer]} {computer.title()}")

        result = determine_winner(player, computer, wins)

        if result == "player":
            print("✅ You win this round!")
            player_score += 1
            total_rounds += 1

        elif result == "computer":
            print("❌ Computer wins this round!")
            computer_score += 1
            total_rounds += 1

        else:
            print("🤝 It's a tie!")

        print(f"\nScore -> You: {player_score} | Computer: {computer_score}")
        print("-" * 40)

    print("\n========== GAME OVER ==========")

    if player_score > computer_score:
        print("🏆 Congratulations! You won the match!")
    else:
        print("💻 Computer won the match!")

    win_percentage = (player_score / total_rounds * 100) if total_rounds else 0

    print(f"\nFinal Score:")
    print(f"You: {player_score}")
    print(f"Computer: {computer_score}")
    print(f"Win Percentage: {win_percentage:.2f}%")
    print("===============================")


if __name__ == "__main__":
    main()