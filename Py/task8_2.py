# Напишите функцию, которая в бесконечном цикле запрашивает имя, личный идентификатор и уровень
# доступа (от 1 до 7).
# После каждого ввода добавляйте новую информацию в
# JSON файл.
# Пользователи группируются по уровню доступа.
# Идентификатор пользователя выступает ключём для имени.
# Убедитесь, что все идентификаторы уникальны независимо
# от уровня доступа.
# При перезапуске функции уже записанные в файл данные
# должны сохраняться.

import json
import os

PATH_DATA = '../json/user_data.json'

def load_json():
    if os.path.exists(PATH_DATA):
        with open(PATH_DATA, 'r', encoding='UTF-8') as f:
            data = json.load(f)
    else:
        data = {}
    return data


def input_name():
    name = input('enter your name: ')
    return name


def input_id(data):
    while True:
        u_id = input('enter your id: ')
        if u_id not in get_list_id(data):
            return u_id


def input_lvl():
    lvl = input('enter your level: ')
    if lvl.isdigit() and 0 < int(lvl) < 8:
        return lvl


def get_list_id(data: dict):
    list_id = set()
    for users in data.values():
        for user in users:
            for key in user.keys():
                list_id.add(key)
    return list_id

def new_user_db():

    while True:
        user_db = load_json()

        name = input_name()
        if not name:
            pass
        u_id = input_id(user_db)
        lvl = input_lvl()

        if lvl in user_db:
            user_db[lvl].append({u_id: name})
        else:
            user_db[lvl] = [{u_id: name}]
        with open(PATH_DATA, 'w',encoding='UTF-8') as file:
            json.dump(user_db,file, indent=4, ensure_ascii=False)
        

new_user_db()