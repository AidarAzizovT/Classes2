example = '922+4+6+8+22'
start = 0
end = 0

for index, value in enumerate(example):
    if value == '+':
        end = index
        num = example[start:end]
        print(num)
        start = end






