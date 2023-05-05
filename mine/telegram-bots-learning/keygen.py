def get_key_by_name(name):
    key = f'WDW1911{str(len(name) + 11)}-'

    for letter in name:
        key += hex(ord(letter))[2:]

    return key.upper()

