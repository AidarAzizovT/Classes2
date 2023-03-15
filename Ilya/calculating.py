input_data = '4+5+6-7-2'
start = 0
end = 0
numbers = []
for index, value in enumerate(input_data):

    if value in ['+', '-']:
        end = index
        number = input_data[start:end]
        start = index
        numbers.append(number)

print(numbers)
print(sum([12, -2, 1]))


# def operate(str1):
#     if str1[0] == '+':
#         num1 = int(str1[1:])
#     elif str1[0] == '-':
#         num1 = -int(str1[1:])
#     else:
#         num1 = None
#     return num1
#
# a = operate('-5')
# print(a, type(a))

#43+46+12+46-77 =
#123+1234

