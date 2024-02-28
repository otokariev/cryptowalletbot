from telebot import TeleBot, types

bot = TeleBot("5140624469:AAFb1IEahts-sLyX29XZHB0xyZ2VfHg6RDs")


@bot.message_handler(commands=['start'])
def hello(message):
    bot.send_message(message.chat.id, 'Hello')


# @bot.message_handler(commands=['test_button'])
# def send_facebook_button(message):
#     '''
#     При нажатии на кнопку переносит по ссылке,
#     которая редиректит на айпи-логгер,
#     который, в свою очередь, редиректит назад на flaskwebblogproject.
#     '''
#     try:
#         # Создаем объект кнопки с ссылкой
#         inline_button = types.InlineKeyboardButton(text="Мой блог", url="https://flaskwebblogproject.pythonanywhere.com/blog/")
#
#         # Создаем объект инлайн-клавиатуры и добавляем в нее кнопку
#         inline_keyboard = types.InlineKeyboardMarkup().add(inline_button)
#
#         # Отправляем инлайн-клавиатуру с кнопкой в ответ на сообщение
#         bot.send_message(message.chat.id, 'Тест кнопки', reply_markup=inline_keyboard)
#
#     except Exception as e:
#         print(e)


if __name__ == "__main__":
    bot.polling(none_stop=True)

# eblanbot2024@gmail.com
# @nixon2022bot
