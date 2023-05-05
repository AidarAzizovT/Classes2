import pandas

file = pandas.read_excel('test.xlsx')
for el in file['Айдар']:
    print(el)