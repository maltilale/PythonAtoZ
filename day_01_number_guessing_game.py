# Game Scenario: Guess the Secret Number
# The program selects a random integer between 1 and 100. The user must guess the number, and the program provides feedback on whether the guess is too high or too low until the user finds the correct answer.

# Input:
# An integer representing the user's guess.
# Example: 45

# Output:
# Feedback on the guess accuracy.
# Example: "Too high! Try again."

# Final success message: "Congratulations! You guessed the number 42 in 5 attempts."
import random

def valid_input(prompt):
    while True:
        try: 
            return int(input(prompt))
        except ValueError:
            print("Invalid entry! Please enter a whole number.")

def play_game():
    rand_num = random.randint(1, 100)
    attempt = 0
    while True:
        guess = valid_input("Enter your guess: ")
        attempt += 1
        if guess < rand_num:
            print(f"Too low! (Attempt {attempt})")
        elif guess > rand_num:
            print(f"Too high! (Attempt {attempt})")
        else:
            print(f"Correct! You won in {attempt} attempts.")
            break

def main():
    while True:
        play_game()
        play_again = str(input("Play again? Y/N ")).strip().lower()
        if play_again != "y":
            print("Thanks for playing")
            break

if __name__ == "__main__":
 main()