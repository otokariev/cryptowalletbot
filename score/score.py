import json

from main2 import bot


def get_score_filename(message):
    chat_type = message.chat.type
    folder = None
    if chat_type == "private":
        folder = "users"
    elif chat_type in ["supergroup", "group"]:
        folder = "groups"
    return f"{folder}/chat_{message.chat.id}_scores.json"


def get_score(message):
    score_file = get_score_filename(message)
    try:
        with open(score_file, 'r') as file:
            scores = json.load(file)
    except FileNotFoundError:
        scores = {}

    if scores:
        sorted_scores = sorted(scores.items(), key=lambda x: x[1], reverse=True)
        score_list = ''
        for user_id, score in sorted_scores:
            user = bot.get_chat_member(message.chat.id, user_id).user
            username = user.username if user.username else f"{user.first_name} {user.last_name}"
            score_list += f"{username}: {score}\n"
        bot.send_message(message.chat.id, '⚡ Top Scores ⚡\n\n' + score_list + f'\nBack to menu ⭐ /menu ⭐')
    else:
        bot.send_message(message.chat.id, "No scores yet!")


def update_user_score(message):
    score_file = get_score_filename(message)
    try:
        with open(score_file, 'r') as file:
            scores = json.load(file)
    except FileNotFoundError:
        scores = {}

    scores[str(message.from_user.id)] = scores.get(str(message.from_user.id), 0) + 1

    with open(score_file, "w", encoding="utf-8") as file:
        json.dump(scores, file, ensure_ascii=False, indent=4)
