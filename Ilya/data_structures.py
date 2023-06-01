import requests

# url_meteo = f'https://api.open-meteo.com/v1/forecast?latitude={3}&longitude={3}&hourly=temperature_2m&hourly=rain'
# url_geo_reverse = f'https://nominatim.openstreetmap.org/reverse?format=xml&lat=52.5487429714954&lon=-1.81602098644987&zoom=18&addressdetails=1'
url_geo_search = f'https://nominatim.openstreetmap.org/search?q=135+pilkington+avenue,+birmingham&format=xml&polygon_geojson=1&addressdetails=1'
#
#
# print(requests.get(url_geo_search).text)
def lst_to_txt(lst):
    with open('db.txt', 'a') as file:
        for elem in lst:
            file.write(elem + '\n')


def txt_to_lst():
    names = []
    with open('db.txt', 'r') as file:
        for line in file:
            names.append(line)
    return names

a = txt_to_lst()
print(a)
names = []

# while True:
#     name = input('Введите имя')
#     names.append(name)
#     if name == '0':
#         lst_to_txt(names)
#         break
