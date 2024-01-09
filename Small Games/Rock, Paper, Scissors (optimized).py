import random

# Mapping user inputs to full names
choices = {"r": "Rock", "p": "Paper", "s": "Scissors"}

# Get the User's input
while True:
    usr = input("Choose - Rock (r), Paper (p), Scissors (s):\n")
    if usr in choices:
        break

# Get the Computer's input
possible_hands = list(choices.keys())
cpu = random.choice(possible_hands)

# Compare both inputs for the game result
if usr == cpu:
    res = "Tie"
elif (usr == "r" and cpu == "s") or (usr == "s" and cpu == "p") or (usr == "p" and cpu == "r"):
    res = "You Win"
else:
    res = "You Lose"

# Translate the result to be readable
usr = choices[usr]
cpu = choices[cpu]

print("CPU: " + cpu + "\nYOU: " + usr + "\nRESULT: " + res)