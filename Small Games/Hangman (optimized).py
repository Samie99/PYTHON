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

print(f"\n\n-----HANGMAN-----")
counter = 0

def choosing_letter(word, chosen_topic):
    global answer, counter

    # Displays the current state of the word with guessed letters
    print(f"\nTOPIC: {chosen_topic}\nWORD: {answer}\n")

    # Loop to get a valid user input for a letter
    while True:
        chosen = input(f"({counter + 1}/{MAX_TRIES}) CHOOSE A LETTER:\n")
        if chosen.isalpha() and len(chosen) == 1:
            break
        continue

    # Updates the answer with correctly guessed letters
    for index, x in enumerate(word):
        if x.lower() == chosen.lower():
            answer = answer[:index] + word[index] + answer[index + 1:]

# Main game loop, allowing the user to guess letters
while counter < MAX_TRIES:
    choosing_letter(word, chosen_topic)
    counter += 1
    # Check if all letters have been guessed
    if "_" not in answer:
        print(f"\nWORD: {word}\n -----YOU WIN-----")
        break

# Checks if there are no underscores left in the answer to determine the win condition
if "_" in answer:
    print(f"\nWORD: {word}\n -----YOU LOSE-----")
