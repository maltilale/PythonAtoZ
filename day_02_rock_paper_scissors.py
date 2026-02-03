# Implementation Scenario
# Your script should prompt the user for a choice, generate a random move for the computer, and then compare the two based on standard game rules. To handle user input safely, it is best to convert the string to lowercase.

# Input:
# user_action = input("Enter a choice (rock, paper, scissors): ").lower()
# possible_actions = ["rock", "paper", "scissors"]
# computer_action = random.choice(possible_actions)

# Output (Example Interaction):
# Enter a choice (rock, paper, scissors): rock
# You chose rock, computer chose scissors.
# Rock smashes scissors! You win!

# Output (Draw Scenario):
# Enter a choice (rock, paper, scissors): paper
# You chose paper, computer chose paper.
# Both players selected paper. It's a tie!


# Winning Rules as follows:
# Rock vs paper-> paper wins
# Rock vs scissor-> Rock wins
# paper vs scissor-> scissor wins.

import random
from typing import NoReturn

OPTIONS = ["r", "p", "s"]
LABELS = {"r": "rock", "p": "paper", "s": "scissors"}

def get_user_choice(prompt: str) -> str:
    while True:
        response = input(prompt).strip().lower()
        if response in OPTIONS:
            return response
        else:
            print("Invalid choice! Please select only one option from "
            f"{', '.join(opt.upper() for opt in OPTIONS)}")

def get_yes_no_input(prompt: str) -> bool:
    while True:
        response = input(prompt).strip().lower()
        if response in ("y", "yes"):
            return True
        elif response in ("n", "no"):
            return False
        print("Please enter 'Y' or 'N'.")

def play_game() -> None:
    computer_choice = random.choice(OPTIONS)
    print(
        f"Decide an option between"
        f" Rock({OPTIONS[0]}), Paper({OPTIONS[1]}), Scissors({OPTIONS[2]})!"
    )
    user_choice = get_user_choice(f"Please enter only 1 option from {", ".join(opt.upper() for opt in OPTIONS)}: ")

    user_choice_idx = OPTIONS.index(user_choice)
    computer_choice_idx = OPTIONS.index(computer_choice)

    print(f"You chose {LABELS[user_choice]}, computer chose {LABELS[computer_choice]}.")

    result = (user_choice_idx - computer_choice_idx) % 3

    if result == 0:
        print("Game Draw!!")
    elif result == 1:
        print("Yay! You win!!")
    else:
        print("Oops! Computer wins!!")

def main() -> NoReturn:
    print(f"-" * 60)
    print("Welcome to the Rock - Paper - Scissor game!")
    print(f"-" * 60)

    try:
        while True:
            play_game()
            play_again = get_yes_no_input("\nPlay again? (Y/N): ")
            if not play_again:
                print("Thanks for playing!")
                break
    except (KeyboardInterrupt, EOFError):
        print("Thanks for playing!")
    
    raise SystemExit(0)

if __name__ == "__main__":
    main()
