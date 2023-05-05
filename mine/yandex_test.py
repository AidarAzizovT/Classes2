
amount_dc, amount_servers, amount_events = list(map(int, input().split(' ')))
data_centers = dict()
commands = list()
R_mul_amount_of_enabled = dict()

for i in range(1, amount_dc + 1):
    data_centers[i] = {'servers': [1] * amount_servers, 'R': 0}


for i in range(amount_events):
    commands.append(input())

for command in commands:
    if 'DISABLE' == command[0:7]:
        command = command.split(' ')
        number_of_dc = int(command[1])
        number_of_server = int(command[2])
        data_centers[number_of_dc]['servers'][number_of_server - 1] = 0

    elif 'RESET' == command[0:5]:
        command = command.split(' ')
        number_of_dc = int(command[1])
        data_centers[number_of_dc]['servers'] = [1] * amount_servers
        data_centers[number_of_dc]['R'] += 1

    else:

        for key, value in data_centers.items():
            R_mul_amount_of_enabled[key] = value['R'] * sum(value['servers'])
        #print(R_mul_amount_of_enabled)

        if command == 'GETMAX':
            # max_value = max(R_mul_amount_of_enabled.values())
            # for i in range(1, len(R_mul_amount_of_enabled) + 1):
            #     if R_mul_amount_of_enabled[i] == max_value:
            #         print(i)
            #         break


            max_value = max(R_mul_amount_of_enabled.items(), key=lambda x: x[1])
            print(max_value[0])
        else:
            min_value = min(R_mul_amount_of_enabled.items(), key=lambda x: x[1])
            print(min_value[0])
            # min_value = min(R_mul_amount_of_enabled.values())
            # for i in range(1, len(R_mul_amount_of_enabled) + 1):
            #     if R_mul_amount_of_enabled[i] == min_value:
            #         print(i)
            #         break
