import random

MAX_TRIES = 5

WORD_LISTS = {
    "Fruits" : ["Apple", "Banana", "Pineapple", "Kiwi", "Orange", "Tomato", "Grape", "Cherry", "Strawberry", "Lime", "Pear", "Melon", "Peach"],
    "Vegetables" : ["Leek", "Beet", "Caper", "Carrot", "Celery", "Garlic", "Lentil", "Fennel", "Cabbage", "Broccoli", "Onion", "Artichoke"],
    "Animals" : ["Dog", "Lion", "Lizard", "Cat", "Bear", "Peacock", "Pig", "Turtle", "Frog", "Fish", "Elephant", "Raccoon", "Zebra"],
    "Companies" : ["Apple", "Tesla", "Mcdonalds", "Walmart", "Toyota", "Sony", "Microsoft", "Disney", "Nestle", "Intel", "Amazon", "Costco"],
    "Foods" : ["Crepe", "Pizza", "Churro", "Sushi", "Taco", "Burger", "Duck", "Pie", "Curry", "Chilaquiles", "Pho", "Bolognese"]
}

# Puts the keywords of the word_lists dictionary, into a list
topics = list(WORD_LISTS.keys())
# Chooses a random topic from the list of topics
chosen_topic = random.choice(topics)
# Chooses a random word from the topic in the word_list dictionary
word = random.choice(WORD_LISTS[chosen_topic])
# Gets the length of the chosen word
let_len = len(word)

answer = ""
length = 1
for count in range(0,let_len):
    answer += f"{length}"
    length += 1

print(f"\n\n-----HANGMAN-----\nTOPIC: {chosen_topic}")
counter = 0

def choosing_letter(word):
    global answer, counter

    print(f"\nWORD: {answer}")
    while True:
        chosen = input(f"({counter+1}/{MAX_TRIES}) CHOOSE A LETTER:\n")
        if chosen.isalpha() and len(chosen) == 1:
            break
        continue
    
    index = 0
    letter_counter = 0

    for x in word:
        if x == chosen.upper() or x == chosen.lower():
            letter_counter += 1

    while chosen.upper() in word and letter_counter > 0:
        index = word.index(str(chosen.upper()))
        answer = (answer[index] == word[index])
        letter_counter -= 1

    while chosen.lower() in word and letter_counter > 0:
        index = word.index(str(chosen.lower()))
        answer = (answer.replace(answer[index], word[index]))
        letter_counter -= 1

while counter < 5:
    choosing_letter(word)
    counter += 1
if answer.isalpha():
    print(f"WORD: {word}\n -----YOU WIN-----")
else:
    print(f"WORD: {word}\n -----YOU LOSE-----")