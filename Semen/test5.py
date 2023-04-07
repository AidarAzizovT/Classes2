example = '922+4+6+8+22'
start = 0
end = 0

for index, value in enumerate(example):
    if value == '+':
        end = index
        num = example[start:end]
        print(num, start, end)
        start = end
    elif index == len(example) - 1:
        end = index
        num = example[start:end+1]
        print(num, start, end)






