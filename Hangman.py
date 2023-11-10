import random

MAX_TRIES = 5

WORD_LISTS = {
    "Fruits" : ["Apple", "Banana", "Pineapple", "Kiwi", "Orange", "Tomato", "Grape", "Cherry", "Strawberry", "Lime", "Pear", "Melon", "Peach"],
    "Vegetables" : ["Leek", "Beet", "Caper", "Carrot", "Celery", "Garlic", "Lentil", "Fennel", "Cabbage", "Broccoli", "Onion", "Artichoke"],
    "Animals" : ["Dog", "Lion", "Lizard", "Cat", "Bear", "Peacock", "Guinea Pig", "Turtle", "Frog", "Fish", "Elephant", "Raccoon", "Zebra"],
    "Companies" : ["Apple", "Tesla", "Mcdonalds", "Walmart", "Toyota", "Sony", "Microsoft", "Disney", "Nestle", "Intel", "Amazon", "Costco"],
    "Foods" : ["Crepe", "Pizza", "Churro", "Sushi", "Taco", "Burger", "Hot Dog", "Peking Duck", "Pie", "Curry", "Chilaquiles", "Pho", "Bolognese"]
}

topics = list(WORD_LISTS.keys())
chosen_topic = random.choice(topics)
chosen_word = random.choice(WORD_LISTS[chosen_topic])
let_len = len(chosen_word)

print(f"-----HANGMAN-----\nTOPIC: {chosen_topic}\n")
counter = 0
while True:
    letter_chosen = input(f"({counter+1}/{MAX_TRIES}) CHOOSE A LETTER:\n")
    if letter_chosen.isdigit() == True:
        continue