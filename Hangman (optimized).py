import random

MAX_TRIES = 10

# Dictionary of word lists organized by topics
WORD_LISTS = {
    "Fruits": ["Apple", "Banana", "Pineapple", "Kiwi", "Orange", "Tomato", "Grape", "Cherry", "Strawberry", "Lime", "Pear", "Melon", "Peach"],
    "Vegetables": ["Leek", "Beet", "Caper", "Carrot", "Celery", "Garlic", "Lentil", "Fennel", "Cabbage", "Broccoli", "Onion", "Artichoke"],
    "Animals": ["Dog", "Lion", "Lizard", "Cat", "Bear", "Peacock", "Pig", "Turtle", "Frog", "Fish", "Elephant", "Raccoon", "Zebra"],
    "Companies": ["Apple", "Tesla", "Mcdonalds", "Walmart", "Toyota", "Sony", "Microsoft", "Disney", "Nestle", "Intel", "Amazon", "Costco"],
    "Foods": ["Crepe", "Pizza", "Churro", "Sushi", "Taco", "Burger", "Duck", "Pie", "Curry", "Chilaquiles", "Pho", "Bolognese"]
}

# Extracts the topics from the WORD_LISTS dictionary
topics = list(WORD_LISTS.keys())
# Chooses a random topic from the list of topics
chosen_topic = random.choice(topics)
# Chooses a random word from the chosen topic in the WORD_LISTS dictionary
word = random.choice(WORD_LISTS[chosen_topic])
# Gets the length of the chosen word
let_len = len(word)

# Initializes the answer with underscores to represent unknown letters
answer = "_" * let_len

print(f"\n\n-----HANGMAN-----\nTOPIC: {chosen_topic}")
counter = 0

def choosing_letter(word):
    global answer, counter

    # Displays the current state of the word with guessed letters
    print(f"\nWORD: {answer}")

    # Loop to get a valid user input for a letter
    while True:
        chosen = input(f"({counter + 1}/{MAX_TRIES}) CHOOSE A LETTER:\n")
        if chosen.isalpha() and len(chosen) == 1:
            break
        continue

    index = 0
    letter_counter = 0

    # Checks if the chosen letter (case insensitive) is in the word
    for x in word:
        if x == chosen.upper() or x == chosen.lower():
            letter_counter += 1

    # Updates the answer with correctly guessed letters
    while chosen.upper() in word and letter_counter > 0:
        index = word.index(str(chosen.upper()))
        answer = answer[:index] + word[index] + answer[index + 1:]
        letter_counter -= 1

    while chosen.lower() in word and letter_counter > 0:
        index = word.index(str(chosen.lower()))
        answer = answer[:index] + word[index] + answer[index + 1:]
        letter_counter -= 1

# Main game loop, allowing the user to guess letters
while counter < 5:
    choosing_letter(word)
    counter += 1

# Checks if there are no underscores left in the answer to determine the win condition
if "_" not in answer:
    print(f"WORD: {word}\n -----YOU WIN-----")
else:
    print(f"WORD: {word}\n -----YOU LOSE-----")
