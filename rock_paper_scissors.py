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

def play_game():
    choices = ["rock", "paper", "scissors"]
    user_input = input(f"Enter choice ({', '.join(choices)}): ").strip().lower()

    if user_input not in choices:
        print("Invalid entry!")
        return

    user_idx = choices.index(user_input)
    comp_idx = random.randint(0, 2)
    
    print(f"You chose {choices[user_idx]}, computer chose {choices[comp_idx]}.")

    result = (user_idx - comp_idx) % 3

    if result == 0:
        print("Game Draw!!")
    elif result == 1:
        print("You win!!")
    else:
        print("Computer wins!!")

if __name__ == "__main__":
    play_game()
