# You are building a simple Mad Libs text game where the program takes user input and fills in placeholders in a story template.

# Given a story template containing placeholders surrounded by curly braces (e.g., {noun}, {verb}, {adjective}), your task is to prompt the user to provide values for each unique placeholder and then replace them with the user inputs to create a complete, funny story.

# Example
# Input Template:
# Today, I went to the {place} to buy a {adjective} {noun}. Then I decided to {verb} all the way home!

# User Input:
# place -> "supermarket"
# adjective -> "giant"
# noun -> "pineapple"
# verb -> "dance"

# Output:
# Today, I went to the supermarket to buy a giant pineapple. Then I decided to dance all the way home!


def mad_lib_game(place: str, adjective: str, noun: str, verb: str) -> str:
    original_words = [place, adjective, noun, verb]
    unique_words = set(original_words)
    if len(original_words) == len(unique_words):
        sentence = f"Today, I went to the {place} to buy a {adjective} {noun}. Then I decided to {verb} all the way home!"
        return sentence
    
    return ""
   

if __name__ == "__main__":
    print("Today, I went to the {place} to buy a {adjective} {noun}. Then I decided to {verb} all the way home!")
    place_text = str(input("In above text, what will be the place? "))
    adjective_text = str(input("In above text, what will be the adjective? "))
    nounplace_text = str(input("In above text, what will be the noun? "))
    verb_text = str(input("In above text, what will be the verb? "))

    result = mad_lib_game(place_text, adjective_text, nounplace_text, verb_text)
    print(result)




