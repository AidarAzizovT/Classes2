# 1. Цикл с предусловием - Loop with a precondition
#
# 2. Рандамизация массива
# 3. Одномерный массив
# 4. Заполнение списков
# 5. Теории чисел
# 6. Корреляция
# 7. Массивы
# 8. Генератор чисел
# 9. Линейный поиск в массиве
# 10. Односвязанные списки
# 11. Быстрая сортировка
# 12. Линейный поиск
# 13. Двоичный поиск
# 14. Стек.Очереди
# 15. Стек с минимумом
# 16. Очереди
# 17. Файлы

#while - пока




# import numpy as np
# import random
#
#
# x = np.array([1, 2, 3, 4, 5])
# y = np.array([1, 2, 3, 4, 5])

# corr_matrix = np.corrcoef(x, y)
# print("Коэффициент корреляции:", corr_matrix)


# promo = input('Input your promo: ')
#
# while True:
#     promo = input('Input your promo: ')
#     if promo == 'summer':
#         print('Sale 100% ')
#         break
#
#


with open('pipes.txt', 'r') as file:
    pipes = dict()
    counter = 1
    for line in file:
        if line == '\n':
            break
        pipes[counter] = int(line)
        counter += 1

    print(pipes)
    working_pipes = file.readline()
    working_pipes = working_pipes.split(' ')
    working_pipes = list(map(int, working_pipes))
    print(working_pipes)

    summary_velocity = 0
    for pipe in working_pipes:
        summary_velocity += 1 / pipes[pipe]

    print(1 / summary_velocity * 60)



total = 0
f = open('pipes.txt', 'r')

for line in f:
  total += int(line)

f.close()

print(total)