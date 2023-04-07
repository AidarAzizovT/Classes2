# while True:
#     try:
#         expr = input("Введите выражение: ")
#         print(eval(expr))
#     except (SyntaxError, NameError, ZeroDivisionError, TypeError, ValueError) as e:
#         print("Ошибка:", e)




def remove_duplicates(s):
    """
    Функция удаляет повторяющиеся символы "+" в строке s
    """
    result = ""
    prev_char = None
    for char in s:
        if not (char == prev_char and char in ['+', '-']):
            result += char
        prev_char = char
    return result

# # Пример использования функции
# s = "aa+b++++++c+d++"
# result = remove_duplicates(s)
# print(result)  # выведет "a+b+c+d+"

def remove_symbols(string):
    lst = list(string)
    index = 0
    while index < len(lst) - 1:
        if lst[index] == lst[index + 1] and lst[index] in ['+', '-']:
            del lst[index]
            index -= 1
        index += 1
    return ''.join(lst)

a = remove_symbols('123++++++43+5')
print(a)

