# Напишите функцию, которая преобразует pickle файл
# хранящий список словарей в табличный csv файл.
# Для тестированию возьмите pickle версию файла из задачи
# 4 этого семинара.
# Функция должна извлекать ключи словаря для заголовков
# столбца из переданного файла.

import pickle
import csv
import json

def open_pickle(file_name: str):
    with open(file_name, 'rb') as f1:
         data = pickle.load(f1)
    return data

def csv_new(name_pickle:str, name_csv:str):
    data = open_pickle(name_pickle)
    heads = list(data.keys())
    rows = list(zip(*list(data.values())))
    with open(name_csv, 'w', encoding='utf-8') as f:
        csv_write = csv.writer(f,dialect='excel', delimiter=' ', lineterminator='\n')
        csv_write.writerow(heads)
        csv_write.writerows(rows)


csv_new('task_6.pickle', 'task6.csv')