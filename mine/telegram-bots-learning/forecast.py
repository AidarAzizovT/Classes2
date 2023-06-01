import requests
import datetime


def change_type_of_date(date_str):
    year = int(date_str[0:4])
    month = int(date_str[5:7])
    day = int(date_str[8:10])
    hour = int(date_str[11:13])
    minute = int(date_str[14:])
    return datetime.datetime(year, month, day, hour, minute)


def get_weather_now(longitude, latitude):
    url = f'https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&hourly=temperature_2m&hourly=rain'
    response = requests.get(url).json()['hourly']
    current_datetime = datetime.datetime.now()
    for time, temperature, rain in zip(response['time'], response['temperature_2m'], response['rain']):
        changed_type_time = change_type_of_date(time)
        if changed_type_time.month == current_datetime.month:
            if changed_type_time.day == current_datetime.day:
                if changed_type_time.hour == current_datetime.hour:
                    return {'temperature': temperature, 'rain': rain}



print(get_weather_now(0, 0))







