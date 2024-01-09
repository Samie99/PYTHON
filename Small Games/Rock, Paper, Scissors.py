import random

# Get the User's input
index = 0
while index == 0:
    usr = input("Choose - Rock (r), Paper (p), Scissors (s):\n")
    if usr in "rps" and len(usr) == 1:
        index += 1
    if index == 1:
        break

# Get the Computers input
possible_hands = ["r", "p", "s"]
cpu = random.choice(possible_hands)

# Compare both inputs for game result
res = ""
if usr == cpu:
    res = "Tie"
elif (usr == "r" and cpu == "s") or (usr == "s" and cpu == "p") or (usr == "p" and cpu == "r"):
    res = "You Win"
elif (usr == "s" and cpu == "r") or (usr == "p" and cpu == "s") or (usr == "r" and cpu == "p"):
    res = "You Lose"

# Translate the result to be readable
if usr == "r":
    usr = "Rock"
elif usr == "p":
    usr = "Paper"
elif usr == "s":
    usr = "Scissors"
if cpu == "r":
    cpu = "Rock"
elif cpu == "p":
    cpu = "Paper"
elif cpu == "s":
    cpu = "Scissors"
print("CPU: "+cpu+"\nYOU: "+usr+"\nRESULT: "+res)