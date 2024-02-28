import time

from main2 import bot
from score.score import update_user_score
from word.word import dictionary
from start.start import continue_game


def check_translation(message, word):
    global hint1, hint2, hint3, timeout, game

    if game:
        translation = message.text.strip().lower()
        if translation == dictionary[word].lower():
            bot.send_message(message.chat.id, "🎯 Exactly! 🎯")

            update_user_score(message)

            hint1.cancel()
            hint2.cancel()
            hint3.cancel()
            timeout.cancel()

            game = False
            time.sleep(1)
            bot.send_message(message.chat.id,
                             "😎 Another word?\n"
                             "✅ Enter 'y'\n")
            bot.register_next_step_handler(message, continue_game)

        else:
            bot.register_next_step_handler(message, check_translation, word)
