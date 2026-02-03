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
from typing import NoReturn

MIN_NUMBER = 1
MAX_NUMBER = 100

def get_valid_guess_input(prompt: str, min_val: int, max_val: int) -> int:
    while True:
        try: 
            input_val = int(input(prompt))
            if min_val <= input_val <= max_val:
                return input_val
            else:
                print(f"Please enter a number between {min_val} and {max_val}.")
        except ValueError:
            print("Invalid entry! Please enter a whole number.")
        except (KeyboardInterrupt, EOFError):
            print("\nGame interrupted")
            raise

def get_yes_no_input(prompt: str) -> bool:
    while True:
        response = input(prompt).strip().lower()
        if response in ('y', 'yes'):
            return True
        if response in ('n', 'no'):
            return False
        print("Please enter 'Y' or 'N'.")

def play_game() -> None:
    random_number = random.randint(MIN_NUMBER, MAX_NUMBER)
    attempt_count = 0
    print(f"Guess the number between {MIN_NUMBER} and {MAX_NUMBER}!")
    while True:
        guess = get_valid_guess_input(
            "Enter your guess: ",
             MIN_NUMBER,
              MAX_NUMBER)
        attempt_count += 1

        if guess < random_number:
            print(f"Too low! (Attempt {attempt_count})")
        elif guess > random_number:
            print(f"Too high! (Attempt {attempt_count})")
        else:
            attempts_text = "attempt" if attempt_count == 1 else "attempts"
            print(f"Correct! You won in {attempt_count} {attempts_text}")
            break

def main() -> NoReturn:
    print("Welcome to the number guessing game!")
    try:
        while True:
            play_game()
            play_again = str(input("\nPlay again? (Y/N): ")).strip().lower()
            if play_again != "y":
                print("Thanks for playing!")
                break
    except (KeyboardInterrupt, EOFError):
        print("\nThanks for playing!")
    
    raise SystemExit(0)

if __name__ == "__main__":
    main()