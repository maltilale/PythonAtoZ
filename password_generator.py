# You are tasked with building a tool that generates a customized, secure password based on user preferences. The script must pull from a pool of letters, numbers, and symbols, then shuffle the final result to ensure the password is not predictable.

# Input
# Number of letters: 8
# Number of symbols: 2
# Number of numbers: 2

# Output
# Generated Password: gH7!kL2#pQ9z

import secrets
import string

LETTERS = string.ascii_letters          # a-zA-Z
DIGITS = string.digits                 # 0-9
SYMBOLS = "!@#$%^&*()-_=+[]{};:,.<>?/" # safe-ish symbol set (customizable)

def generate_password(n_letters: int, n_symbols: int, n_numbers: int) -> str:
    if min(n_letters, n_symbols, n_numbers) < 0:
        raise ValueError("Counts cannot be negative.")

    chars = []
    chars += [secrets.choice(LETTERS) for _ in range(n_letters)]
    chars += [secrets.choice(SYMBOLS) for _ in range(n_symbols)]
    chars += [secrets.choice(DIGITS) for _ in range(n_numbers)]

    secrets.SystemRandom().shuffle(chars) 
    return "".join(chars)

if __name__ == "__main__":
    n_letters = int(input("Number of letters: "))
    n_symbols = int(input("Number of symbols: "))
    n_numbers = int(input("Number of numbers: "))

    password = generate_password(n_letters, n_symbols, n_numbers)
    print(f"Generated Password: {password}")
