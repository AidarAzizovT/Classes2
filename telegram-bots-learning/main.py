from config import TOKEN
import telebot

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(['hi'])
def hi_handler(message):
    bot.send_message(message.chat.id, 'salam')

bot.polling()