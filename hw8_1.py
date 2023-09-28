# Напишите функцию, которая получает на вход директорию и рекурсивно
# обходит её и все вложенные директории. Результаты обхода сохраните в
# файлы json, csv и pickle.
# ○ Для дочерних объектов указывайте родительскую директорию.
# ○ Для каждого объекта укажите файл это или директория.
# ○ Для файлов сохраните его размер в байтах, а для директорий размер файлов в ней с учётом всех вложенных
# файлов и директорий.
# Соберите из созданных на уроке и в рамках домашнего задания функций
# пакет для работы с файлами разных форматов.

import os
import json
import pickle
import csv
import pathlib


def get_dir_size(path: str = os.getcwd()):
    total = 0
    with os.scandir(path) as it:
        for entry in it:
            if entry.is_file():
                total += os.path.getsize(entry)
            elif entry.is_dir():
                total += get_dir_size(entry.path)
    return total


def dirtree_info(path: str = os.getcwd()):
    dirtree_dic = {}
    for files in os.walk(path):
        for file in files[1]:
            dirtree_dic[file] = ['директория', files[0], get_dir_size(os.path.join(files[0],file))]
        for file in files[2]:
            dirtree_dic[file] = ['файл', files[0], os.path.getsize(os.path.join(files[0],file))]
    return dirtree_dic


with open('dirtree.json', 'w', encoding='UTF-8') as f_1:
    json.dump(dirtree_info(), f_1, indent='\t', ensure_ascii=False)

with open('dirtree.csv', 'w', newline='', encoding='UTF-8') as f_2:
    dict_tree = dirtree_info()
    csv_lst = []
    for key, value in dict_tree.items():
        csv_line = []
        csv_line.append(key)
        for data in value:
            csv_line.append(data)
        csv_lst.append(csv_line)
    csv_file = csv.writer(f_2, dialect='excel', delimiter=' ', lineterminator='\n')
    csv_file.writerows(csv_lst)

with open('dirtree.pickle', 'wb') as f_3:
    pickle.dump(dirtree_info(), f_3)


