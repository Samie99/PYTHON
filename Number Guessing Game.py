import random
word_dict = {0: "1st", 1: "2nd", 2: "3rd"}

print("Both you and the CPU have 3 tries to guess the other's number.")
while True:
    mode = input("Want to choose a number or guess?\nType (c) to choose or (g) to guess:\n")
    if mode in "cg" and len(mode) == 1:
        break

def choose_mode():
    while True:
        usr_choice = input("Choose a number between 0 and 10:\n")
        if usr_choice.isdigit() is False:
            continue
        if 10 >= int(usr_choice) >= 0:
            break
    counter = 0
    min_num = 0
    max_num = 10
    while counter <= 3:
        if counter == 3:
            print("-----You Win-----")
            break
        cpu_guess = random.randint(min_num, max_num)
        print(f"{word_dict[counter]} Number: {cpu_guess}")
        usr_reply = input("Is my number HIGHER (h), LOWER (l), or CORRECT (c):\n")
        if usr_reply == "h":
            counter += 1
            max_num = cpu_guess - 1
        elif usr_reply == "l":
            counter += 1
            min_num = cpu_guess + 1
        elif usr_reply == "c":
            print(f"CPU's GUESS: {cpu_guess}\nYOUR NUMBER: {usr_choice}\nCOMPARISON: {(int(cpu_guess) == int(usr_choice))}")
            break
choose_mode()