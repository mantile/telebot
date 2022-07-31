import telebot
from telebot import types

bot = telebot.TeleBot('5476681854:AAHDpCQxxVRzrnumlu16q-SbR4NcTX3AYEs')


@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("🏠 Главное меню 🏠")
    btn2 = types.KeyboardButton("❓ Помощь ❓")
    markup.add(btn1, btn2)
    bot.send_message(message.chat.id,
                     text="Привет, {0.first_name}! Я музыкальный бот для поиска и скачивания песен!".format(
                         message.from_user), reply_markup=markup)


@bot.message_handler(content_types=['text'])
def func(message):
    if (message.text == "🏠 Главное меню 🏠"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("💿 Поиск трека по названию 💿")
        btn2 = types.KeyboardButton("🔡 Поиск трека по тексту 🔡")
        btn3 = types.KeyboardButton("🔀 Случайный трек 🔀")
        btn4 = types.KeyboardButton("🎧 Чарт ВК 🎧")
        back = types.KeyboardButton("🔙 Назад 🔙")
        markup.add(btn1, btn2, btn3, btn4, back)
        bot.send_message(message.chat.id, text="Вот, что могу предложить:", reply_markup=markup)
    elif (message.text == "❓ Помощь ❓"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("🤓 Что я могу? 🤓")
        btn2 = types.KeyboardButton("📣 Обратная связь 📣")
        back = types.KeyboardButton("🔙 Назад 🔙")
        markup.add(btn1, btn2, back)
        bot.send_message(message.chat.id, text="Задай мне вопрос", reply_markup=markup)

    elif (message.text == "🤓 Что я могу? 🤓"):
        bot.send_message(message.chat.id, "Еще раз привет! Давай расскажу, что я могу: \n\nЯ могу найти песню по ее названию\n\nМогу помочь найти трек по тексту\n\nМожем послушать, что сейчас в топе ВК\n\nА можем запустить случайный трек")

    elif message.text == "📣 Обратная связь 📣":
        bot.send_message(message.chat.id, text="@Mantile")

    elif (message.text == "🔙 Назад 🔙"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("🏠 Главное меню 🏠")
        btn2 = types.KeyboardButton("❓ Помощь ❓")
        markup.add(btn1, btn2)
        bot.send_message(message.chat.id, text="Мы снова тут", reply_markup=markup)
    elif (message.text == "💿 Поиск трека по названию 💿"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn2 = types.KeyboardButton("🔙 Назад 🔙")
        markup.add(btn2)
        bot.send_message(message.chat.id, text="🆕 Отправь мне название трека 🆕", reply_markup=markup)

    else:
        bot.send_message(message.chat.id, text="Тут я даже не знаю, что тебе сказать...")


bot.polling(none_stop=True)