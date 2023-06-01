def check(num1, num2):
    return (num1 - num2) % 2 == 0 and (num1 % 17 == 0 or num2 % 17 == 0)

with open('27991_B (1).txt', 'r') as file:
    numbers = file.readlines()[1:]
numbers = list(map(int, numbers))
numbers.sort()


global_high = len(numbers) - 1
global_low = 0

loc_high = global_high
loc_low = loc_high - 1

num1 = 0
num2 = 0
while True:
    while global_low < loc_low:
        if check(numbers[loc_high], numbers[loc_low]):
            if numbers[loc_low] + numbers[loc_high] > num1 + num2:
                num1, num2 = numbers[loc_low], numbers[loc_high]
                break
        loc_low -= 1
    if loc_high - loc_low < 3:
        break
    global_high = loc_high-1
    global_low = loc_low

    loc_high = global_high
    loc_low = loc_high - 1
print(num1, num2)
