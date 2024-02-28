import telebot
# from flask import Flask, request

from config import TOKEN2

bot = telebot.TeleBot(TOKEN2)  # threaded=False

# app = Flask(__name__)

# URL = ('https://englishteacherbot.pythonanywhere.com/' +
#        '51b9e4b9cbd872e827c45f9db4a6c002611bd9a2437a4f278066282abc2f3a40')
#
# bot.remove_webhook()
# bot.set_webhook(url=URL)
#
#
# @app.route('/' + '51b9e4b9cbd872e827c45f9db4a6c002611bd9a2437a4f278066282abc2f3a40', methods=['POST'])
# def webhook():
#     update = telebot.types.Update.de_json(request.stream.read().decode('utf-8'))
#     bot.process_new_updates([update])
#     return 'ok', 200


if __name__ == "__main__":
    bot.polling(none_stop=True)
