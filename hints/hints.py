import random
import time

from main2 import bot
from word.word import dictionary
from start.start import continue_game


def get_hint1(message, word):
    translation = dictionary[word]
    stars = '*' * len(translation)
    index = random.randint(0, len(translation) - 1)
    stars = stars[:index] + translation[index] + stars[index + 1:]
    bot.send_message(message.chat.id, stars)


def get_hint2(message, word):
    translation = dictionary[word]
    stars = '*' * len(translation)
    indices = random.sample(range(len(translation)), 2)
    for index in indices:
        stars = stars[:index] + translation[index] + stars[index + 1:]
    bot.send_message(message.chat.id, stars)


def get_hint3(message, word):
    translation = dictionary[word]
    stars = '*' * len(translation)
    indices = random.sample(range(len(translation)), 3)
    for index in indices:
        stars = stars[:index] + translation[index] + stars[index + 1:]
    bot.send_message(message.chat.id, stars)


def run_timeout(message, word):
    bot.send_message(message.chat.id, f"The correct translation is:\n✨ {dictionary[word]} ✨")
    game = False
    time.sleep(1)
    bot.send_message(message.chat.id,
                     "😎 Another word?\n"
                     "✅ Enter 'y'\n")
    bot.register_next_step_handler(message, continue_game)
