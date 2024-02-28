import time
import random
import threading

from main2 import bot
from word.word import dictionary
from hints.hints import get_hint1, get_hint2, get_hint3, run_timeout


from check.check import check_translation

hint1: threading.Timer | None
hint2: threading.Timer | None
hint3: threading.Timer | None
timeout: threading.Timer | None

game = False


@bot.message_handler(commands=['play'])
def start_game(message):
    global hint1, hint2, hint3, timeout, game

    game = True

    if game:
        time.sleep(1)
        word = random.choice(list(dictionary.keys()))
        bot.send_message(message.chat.id, f"Ok! 😎\nTranslate this word, please:\n✨ {word} ✨")

        hint1 = threading.Timer(10.0, get_hint1, args=[message, word])
        hint2 = threading.Timer(20.0, get_hint2, args=[message, word])
        hint3 = threading.Timer(30.0, get_hint3, args=[message, word])
        timeout = threading.Timer(40.0, run_timeout, args=[message, word])

        hint1.start()
        hint2.start()
        hint3.start()
        timeout.start()

        bot.register_next_step_handler(message, check_translation, word)


def continue_game(message):
    if message.text.lower() == 'y':
        start_game(message)
    else:
        bot.send_message(message.chat.id,
                         f'See you later 😎\n'
                         'Back to menu ⭐ /menu ⭐')
