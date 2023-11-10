import random

# Global constants that will change values within functions
MAXIMUM_VALUE = 100
MINIMUM_VALUE = 0
AMOUNT_OF_TRIES = 10

# Dictionaries to keep count of CPU guesses and whether the player wins/loses
word_dict = {1: "1st", 2: "2nd", 3: "3rd"}
outcome = {True: "----------YOU WIN----------", False: "----------YOU LOSE----------"}

# Prints the rules and gets input for what mode the player decides
print(f"Both you and the CPU have {AMOUNT_OF_TRIES} tries to guess the other's number.")
while True:
    mode = input("Want to choose a number or guess?\nType (c) to choose or (g) to guess:\n")
    if mode in "cg" and len(mode) == 1:
        break

# "Choose" mode function
def choose_mode():
    global MAXIMUM_VALUE, MINIMUM_VALUE, AMOUNT_OF_TRIES

    # Loop that only stops when player input is a single whole integer
    while True:
        usr_choice = input(f"\nChoose a number between {MINIMUM_VALUE} and {MAXIMUM_VALUE}:\n")
        if usr_choice.isdigit() is False:
            continue
        if MAXIMUM_VALUE >= int(usr_choice) >= MINIMUM_VALUE:
            break

    # Gathers global and local variables
    counter = 1
    word_count = 4
    while counter <= AMOUNT_OF_TRIES + 1:
        if counter == AMOUNT_OF_TRIES + 1:
            print(f"\nCPU's NUMBER: {cpu_guess}\nYOUR NUMBER: {usr_choice}\n{outcome[(int(cpu_guess) == usr_choice)]}")
            break
        # Generates a randome integer between the min and max
        cpu_guess = random.randint(MINIMUM_VALUE, MAXIMUM_VALUE)
        print(f"\n{word_dict[counter]} Number: {cpu_guess}")
        if int(usr_choice) == cpu_guess:
            print(f"\nCPU's NUMBER: {cpu_guess}\nYOUR NUMBER: {usr_choice}\n{outcome[(cpu_guess == int(usr_choice))]}")
            break
        while True:
            usr_reply = input(f"Is your number HIGHER (h) or LOWER (l) than {cpu_guess}?\n")
            if usr_reply in "hl" and len(usr_reply) == 1:
                break
        # depending on the player input, the counter increases, and the min/max increases/decreases
        if (usr_reply == "h" and cpu_guess == MAXIMUM_VALUE) or (usr_reply == "l" and cpu_guess == MINIMUM_VALUE):
            print(f"\nCPU's NUMBER: {cpu_guess}\nYOUR NUMBER: {usr_choice}\n{outcome[(cpu_guess == int(usr_choice))]}")
            break
        if usr_reply == "h":
            counter += 1
            MINIMUM_VALUE = cpu_guess + 1
            word_dict.update({word_count:f"{word_count}th"})
            word_count += 1
        else:
            counter += 1
            MAXIMUM_VALUE = cpu_guess - 1
            word_dict.update({word_count:f"{word_count}th"})
            word_count += 1

# "Guess" mode function
def guess_mode():
    global MAXIMUM_VALUE, MINIMUM_VALUE, AMOUNT_OF_TRIES
    cpu_choice = random.randint(MINIMUM_VALUE, MAXIMUM_VALUE)
    print("\nNumber chosen.")
    counter = 1
    while counter <= AMOUNT_OF_TRIES + 1:
        if counter == AMOUNT_OF_TRIES + 1:
            print(f"\nCPU's NUMBER: {cpu_choice}\nYOUR NUMBER: {usr_guess}\n{outcome[(cpu_choice == int(usr_guess))]}")
        while True:
            usr_guess = input(f"Choose a number between {MINIMUM_VALUE} and {MAXIMUM_VALUE}:\n")
            if usr_guess.isdigit() is False:
                continue
            if MAXIMUM_VALUE >= int(usr_guess) >= MINIMUM_VALUE:
                break
        if int(usr_guess) == cpu_choice:
            print(f"\nCPU's NUMBER: {cpu_choice}\nYOUR NUMBER: {usr_guess}\n{outcome[(cpu_choice == int(usr_guess))]}")
            break
        elif int(usr_guess) > cpu_choice:
            print(f"\nGUESS NUMBER {counter}: Too High.")
            counter += 1
        else:
            print(f"\nGUESS NUMBER {counter}: Too Low.")
            counter += 1

# Runs "guess" game mode
if mode == "g":
    guess_mode()

# Runs "choose" game mode
if mode == "c":
    choose_mode()