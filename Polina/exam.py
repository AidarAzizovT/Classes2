def turn_file_in_list(filename='flower_drum.txt'):
    colors = []
    with open('flower_drum.txt', 'r', encoding='utf-8') as file:
        for line in file:
            color_name = line.split('#')[0][:-1]
            hex_code = '#' + line.split('#')[1].split(' ')[0]
            rgb = tuple(map(int, line.split(' ')[-3:]))
            colors.append([color_name, hex_code, rgb])
    return colors


print(turn_file_in_list())

def find_color_by_name(color_name):
    colors = turn_file_in_list()
    for elem in colors:
        if elem[0] == color_name:
            elem[2] = tuple(map(str, elem[2]))
            elem[2] = ' '.join(elem[2])
            return elem

def find_color_by_hex_code(hex_code):
    colors = turn_file_in_list()
    for elem in colors:
        if elem[1] == hex_code:
            elem[2] = tuple(map(str, elem[2]))
            elem[2] = ' '.join(elem[2])
            return elem

def find_color_by_rgb(rgb):
    colors = turn_file_in_list()
    for elem in colors:
        if elem[2] == rgb:
            elem[2] = tuple(map(str, elem[2]))
            elem[2] = ' '.join(elem[2])
            return elem


def color_search(*input_colors, filename='output.txt'):
    if type(input_colors[0]) == tuple:
        print('It is rgbs!')
        with open(filename, 'w') as file:
            for rgb in input_colors:
                file.write(*find_color_by_rgb(rgb) + '\n')

    elif input_colors[0].startswith('#'): #hex
        print('It is hex - codes!')
        with open(filename, 'w') as file:
            for hex_code in input_colors:
                file.write()
    else:
        print('It is name of colors!')
        with open(filename, 'w', encoding='utf-8') as file:
            for color_name in input_colors:
                result = find_color_by_name(color_name)
                file.write(' '.join(result))










# def dict_flip(*args):
#     d = {}
#     for i in range(0, len(args), 2):
#         print(args[i].decode('utf-8'))
#     return d
#
#
# lines = [b'\xd0\xa2\xd0\xbe\xd0\xbb\xd1\x81\xd1\x82\xd0\xbe\xd0\xb9',
#          b'\xd0\x94\xd0\xb5\xd1\x82\xd1\x81\xd1\x82\xd0\xb2\xd0\xbe',
#          b'\xd0\x93\xd0\xbe\xd1\x80\xd1\x8c\xd0\xba\xd0\xb8\xd0\xb9',
#          b'\xd0\x94\xd0\xb5\xd1\x82\xd1\x81\xd1\x82\xd0\xb2\xd0\xbe',
#          b'Carroll',
#          b'Alice in Wonderland',
#          b'Shakespeare',
#          b'Hamlet',
#          b'1 \xd1\x8f\xd0\xbd\xd0\xb2\xd0\xb0\xd1\x80\xd1\x8f',
#          b'\xd0\x9d\xd0\xbe\xd0\xb2\xd1\x8b\xd0\xb9 \xd0\xb3\xd0\xbe\xd0\xb4',
#          b'1 \xd0\xbc\xd0\xb0\xd1\x80\xd1\x82\xd0\xb0',
#          b'\xd0\x9d\xd0\xbe\xd0\xb2\xd1\x8b\xd0\xb9 \xd0\xb3\xd0\xbe\xd0\xb4']
# print(dict_flip(*lines))

