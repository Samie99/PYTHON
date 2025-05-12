import random

# USE .RANDINT()
# Random Color Hex
hex_color_code = '#'
for x in range(6):
    hex_color_code = hex_color_code + str(random.randint(0,9))
print(f'Random Hex Color Code:\n{hex_color_code}')

# Random Alphabetical String
random_num_string = ''
random_chr_string = ''
for x in range(10):
    for y in range(8):
        random_num_string = random_num_string + str(random.randint(0,1))
    random_chr_string = random_chr_string + chr(int(random_num_string, 2))
    random_num_string = ''
print(f'Random Character String:\n{random_chr_string}')

# Random Values
print(random.randint(0, 70))