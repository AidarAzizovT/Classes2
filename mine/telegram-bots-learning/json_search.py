import json


def get_coordinates_by_user_id(user_id):
    file = open('addresses.json')
    data = json.load(file)
    return data.get(str(user_id))


def add_user_in_json(user_id, new_data, filename='addresses.json'):
    with open('addresses.json', encoding='utf8') as f:  # Открываем файл
        data = json.load(f)
    data[user_id] = new_data
    with open('addresses.json', 'w', encoding='utf8') as outfile:
        json.dump(data, outfile, indent=3)

