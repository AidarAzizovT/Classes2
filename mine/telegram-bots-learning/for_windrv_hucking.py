import telebot
from config import TOKEN
from telebot import types
from keygen import get_key_by_name

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start_handler(message):
    kb = types.InlineKeyboardMarkup()
    btn1 = types.InlineKeyboardButton('WinDrvGhost', callback_data='WinDrvGhost')
    kb.add(btn1)
    bot.send_message(message.chat.id, 'Hey, I am a huck-bot \nI can give you a key for next apps, but only if you will ask me politely. Choose app, which you want and say me please', reply_markup=kb, )


@bot.callback_query_handler(func=lambda callback: callback.data == 'WinDrvGhost')
def win_drv_ghost_handler(callback):
    mes = bot.send_message(callback.message.chat.id, 'I got you, so send me your name')
    bot.register_next_step_handler(mes, send_key)

def send_key(message):
    bot.send_message(message.chat.id, f'This is your key, {message.text}\n{get_key_by_name(message.text)}')
    mes = bot.send_message(message.chat.id, 'You can write some feedback about me, if you want :)')

    bot.register_next_step_handler(mes, thank_sender)


def thank_sender(message):
    bot.send_message(message.chat.id, 'Thank you for your feedback!')
bot.polling()

