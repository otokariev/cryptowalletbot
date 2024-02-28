import json

from main2 import bot

DICTIONARY = 'dictionaries/custom_dictionary.json'

try:
    with open(DICTIONARY, 'r') as f:
        dictionary = json.load(f)
except FileNotFoundError:
    dictionary = {}


def view_words(message):
    if dictionary:
        words_list = "\n".join([f"{word}: {translation}" for word, translation in dictionary.items()])
        bot.send_message(message.chat.id,
                         f'List of words with translations:\n\n{words_list}\n\n'
                         'Back to menu /menu 📋')
    else:
        bot.send_message(message.chat.id, "The dictionary is empty!")


def add_word(message):
    bot.send_message(message.chat.id, "Please enter the word you want to add (RUSSIAN/UKRAINIAN):")
    bot.register_next_step_handler(message, check_word)


def check_word(message):
    word = message.text.strip().upper()
    if word in dictionary:
        bot.send_message(message.chat.id,
                         f" ❌ The word '{word}' already exists in the dictionary ❌\n"
                         "Back to menu ⭐ /menu ⭐")
    else:
        bot.send_message(message.chat.id, f"Please enter the translation for the word '{word}':")
        bot.register_next_step_handler(message, get_translation, word)


def get_translation(message, word):
    translation = message.text.strip().upper()
    dictionary[word] = translation
    bot.send_message(message.chat.id,
                     f'The word "{word}" with translation "{translation}" has been added successfully!\n'
                     f'Back to menu ⭐ /menu ⭐')

    with open(DICTIONARY, "w", encoding="utf-8") as file:
        json.dump(dictionary, file, ensure_ascii=False, indent=4)
