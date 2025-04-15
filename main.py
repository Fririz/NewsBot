

import telebot
from telebot import types
from secr import TOKEN 
import pars

bot = telebot.TeleBot(TOKEN)

chat_id = 688419885

parser = pars.prs("https://itc.ua/techno/")

print(parser)

"""
if __name__ == "__main__":
    main()
    
markup = types.ReplyKeyboardMarkup(row_width=2)
markup.add(types.KeyboardButton('Подивитись останні новини'), types.KeyboardButton('smthing'))

#bot.send_message(chat_id, "Choose one letter:", reply_markup=markup)



@bot.message_handler(commands=['Подивитись останні новини'])
def echo_all(message):
    bot.send_message(message.chat.id, "aboba")


bot.infinity_polling()
"""