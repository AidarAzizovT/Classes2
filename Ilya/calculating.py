def cut(input_data):
    input_data += 'e'
    if input_data[0] not in ['+', '-']:
        input_data = '+' + input_data

    start = 0
    numbers = []

    for index, value in enumerate(input_data):
        if value in ['+', '-', '*', '/', 'e']:
            number = input_data[start:index]
            start = index
            numbers.append(number)

    return numbers[1:]


def operate(str1):
    if str1[0] == '+':
        num1 = float(str1[1:])
    elif str1[0] == '-':
        num1 = -float(str1[1:])
    else:
        num1 = None
    return num1


def mul_div(cutted):
    operations = {'*(': lambda x, y : x * y,
    '*' : lambda x,y : x * y,
    '/(' : lambda x, y : x / y, '/' : lambda x, y : x / y}

    for index, value in enumerate(cutted):
        if value in ['*(', '/(']:  # second operand is negative
            first_num = cutted[index - 1]
            second_num = cutted[index + 1][:-1]
            first_num = operate(first_num)
            second_num = operate(second_num)
            result = operations[value](first_num, second_num)
            if result > 0:
                cutted[index] = '+' + str(result)
            else:
                cutted[index] = str(result)
            del cutted[index + 1]
            del cutted[index - 1]

        elif value[0] in ['*', '/']:  # second multiplier is positive
            first_num = cutted[index - 1]
            second_num = cutted[index][1:]
            first_num = operate(first_num)
            second_num = int(second_num)
            result = operations[value[0]](first_num, second_num)
            if result > 0:
                cutted[index] = '+' + str(result)
            else:
                cutted[index] = str(result)
            del cutted[index - 1]



def calculate(input_data):
    cutted = cut(input_data)
    mul_div(cutted)
    operated = list(map(operate, cutted))
    result = sum(operated)
    return result

print(calculate('12+5+3+8'))