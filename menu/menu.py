from main2 import bot


@bot.message_handler(commands=['menu'])
def get_menu(message):
    bot.send_message(message.chat.id,
                     f'Welcome to bot menu 🇬🇧\n\n'
                     '🚀 Start is here 👉 /play 👈\n'
                     '🥇 Check the score 👉 /top 👈\n'
                     '📌 Add new word 👉 /add 👈\n')  # 'To check all words press /words 🔡'


@bot.message_handler(commands=['start'])
def hello(message):
    bot.send_message(message.chat.id,
                     'Hello! 😎\nI am a English teacher bot 🇬🇧\n'
                     'If you want to learn some new words,\njust press /play and try me 😉\n'
                     'Back to menu ⭐ /menu ⭐')
