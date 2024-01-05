import json


def add_to_file(words_list: list, user_id: str):
    with open('db.json', encoding='utf-8') as f:
        data = json.load(f)
        if user_id in data:
            if words_list[0] not in [db_words[0] for db_words in data[user_id]['words']]:
                data[user_id]['words'].append(words_list)
            else:
                for db_words in data[user_id]['words']:
                    if db_words[0] == words_list[0]:
                        db_words += words_list[1:]
                        break
        else:
            data[user_id] = {'words': [words_list]}
        with open('db.json', 'w', encoding='utf-8') as outfile:
            json.dump(data, outfile, ensure_ascii=False, indent=2)


def get_from_file(user_id: str):
    with open('db.json', encoding='utf-8') as f:
        data = json.load(f)
    return data[user_id]['words']
