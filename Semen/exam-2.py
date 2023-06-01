import math
with open('27989_B (1).txt', 'r') as file:
    numbers = file.readlines()
    numbers = list(map(int, numbers))[1:]

div_0 = 0
div_2 = 0
div_13 = 0
div_26 = 0

for elem in numbers:
    if elem % 26 == 0:
        div_26 += 1
    elif elem % 13 == 0:
        div_13 += 1
    elif elem % 2 == 0:
        div_2 += 1
    else:
        div_0 += 1

print(div_26 * div_0 + div_26 * div_13 + div_26 * div_2 + div_13 * div_2 + div_26 * (div_26 - 1) /2)
