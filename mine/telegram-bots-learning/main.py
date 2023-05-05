from config import TOKEN
import telebot
from telebot import types
from forecast import get_weather_now
from json_search import get_coordinates_by_user_id, add_user_in_json

bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['start'])
def start_handler(message):
    kb = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    btn1 = types.KeyboardButton(text='Send Location', request_location=True)
    btn2 = types.KeyboardButton(text='Send Phone Number', request_contact=True)
    kb.add(btn1, btn2)
    text = f'Hey, I am bot, which can show you weather right now, right here. \n May you send me your location?'
    bot.send_message(message.chat.id, text, reply_markup=kb)
    #print(message.text)
    #add_user_in_json(message.from_user.id, { "longitude": "12","latitude": "56"})

@bot.message_handler(content_types=['location'])
def location_handler(message):
    kb = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    btn1 = types.KeyboardButton(text='Weather Now')
    btn2 = types.KeyboardButton(text='Change City', request_location=True)
    kb.add(btn1, btn2)
    if get_coordinates_by_user_id(message.from_user.id) is None:
        add_user_in_json(message.from_user.id, { "longitude": str(message.location.longitude),"latitude": str(message.location.longitude)})
        bot.send_message(message.chat.id,
                         'I successfully added you in my Data Base \n Now I am able to forecast weather for you!',
                         reply_markup=kb)

    else:
        add_user_in_json(message.from_user.id,
                         {"longitude": str(message.location.longitude), "latitude": str(message.location.longitude)})
        bot.send_message(message.chat.id,
                         'I successfully changed your location in my Data Base',
                         reply_markup=kb)




@bot.message_handler(func=lambda message :  'Weather' in message.text)
def send_weather(message):
    coordinates = get_coordinates_by_user_id(str(message.chat.id))
    print(message.chat.id)
    print(coordinates)
    if coordinates is not None:
        latitude = coordinates['latitude']
        longitude = coordinates['longitude']
        weather = get_weather_now(longitude, latitude)
        string = f'Temperature now is {weather["temperature"]}, precipitations - {weather["rain"]} milimmetres'
        kb = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
        btn1 = types.KeyboardButton(text='Weather Now')
        btn2 = types.KeyboardButton(text='Change City', request_location=True)
        kb.add(btn1, btn2)
        bot.send_message(message.chat.id, string, reply_markup=kb)
        print(message)
    else:
        bot.send_message(message.chat.id, 'Sorry, we cold not find you in our base :(')
        print(message.chat)
        bot.send_message(message.chat.id, 'Do you want that we add you?')



@bot.message_handler(func=lambda message : 'rate' in message.text)
def rate(message):
    kb = types.InlineKeyboardMarkup()
    btn1 = types.InlineKeyboardButton('Yeeees!', callback_data='btn1')
    kb.add(btn1)
    bot.send_message(message.chat.id, 'Hey! Do you wanna rate us?', reply_markup=kb)


@bot.callback_query_handler(func=lambda callback: callback.data != None)
def callback_handler(callback):
    sent_message = bot.send_message(callback.message.chat.id,
            f'Thank you, {callback.message.chat.first_name} for your wish!. '
            f'\n You can write anything here, we will read everything!')
    bot.register_next_step_handler(sent_message, review)


def review(message):
    with open('feedbacks.txt', 'a') as file:
        file.write(message.text + '\n\n')
    bot.send_message(message.chat.id, 'Thank you again for your feedback!')

@bot.message_handler(content_types=['contact'])
def check_contact(message):
    print(message.contact)
    print(message.from_user)
    print(message.chat)
    bot.send_message('@azizovaidar', 'Some very useful information')

@bot.message_handler(func=lambda message:  'id' in message.text )
def get_id(message):
    bot.send_message(message.chat.id, f'Id of this channel is {message.chat.id}')
bot.polling()

