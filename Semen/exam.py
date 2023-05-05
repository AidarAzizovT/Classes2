diff = []
with open('27-A_demo (1).txt', 'r') as file:
    file.readline()
    summ = 0
    for line in file:
        lst = list(map(int, line.split()))

        diff.append(abs(lst[0] - lst[1]))


        summ += max(lst)
print(summ)
print(diff)
