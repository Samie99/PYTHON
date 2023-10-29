import random

mode = input("Want to choose a number or guess?\n Type (c) to be the chooser or (g) to be the guesser:\n ")
possible_numbers = range(0,9999)

if mode == "c":
    choice = input("Choose a number between 0 and 9999:\n")
if mode == "g":
    cpu_choice = random.choice(possible_numbers)


