
import usersData
import telebot
from telebot import types
from secr import TOKEN 
import pars

bot = telebot.TeleBot(TOKEN)

#chat_id = 688419885



user_pages = {}

@bot.message_handler(commands=['start'])
def send_welcome(message):
    db = usersData.usrDataEdit()
    if db.checkIDInDataBase(message.chat.id):
        db.addUsersToDataBase(message.chat.id, message.from_user.username)
        print(f"Добавляю пользователя: {message.chat.id}, {message.from_user.username}")
    
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn_news = types.KeyboardButton("Подивитись новини")
    btn_prev = types.KeyboardButton("⬅️ Назад")
    btn_next = types.KeyboardButton("➡️ Вперед")
    markup.add(btn_news)
    markup.add(btn_prev, btn_next)
    bot.send_message(message.chat.id, "Привіт, натисни кнопку нижче щоб побачити новини", reply_markup=markup)

    
@bot.message_handler(func=lambda message: message.text == "Подивитись новини")
def show_news(message):
    user_id = message.chat.id
    parser = pars.prs(f"https://www.unian.ua/techno?page={user_pages.get(user_id, 1)}")
    bot.send_message(message.chat.id, parser)

@bot.message_handler(func=lambda message: message.text == "⬅️ Назад")
def go_back(message):
    user_id = message.chat.id
    user_pages[user_id] = max(1, user_pages.get(user_id, 1) - 1)
    bot.send_message(user_id, f"⬅️ Сторінка: {user_pages[user_id]}")


@bot.message_handler(func=lambda message: message.text == "➡️ Вперед")
def go_forward(message):
    user_id = message.chat.id
    user_pages[user_id] = user_pages.get(user_id, 1) + 1
    bot.send_message(user_id, f"➡️ Сторінка: {user_pages[user_id]}")

bot.polling()