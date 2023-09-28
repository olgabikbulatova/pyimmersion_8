# Прочитайте созданный в прошлом задании csv файл без
# использования csv.DictReader.
# Дополните id до 10 цифр незначащими нулями.
# В именах первую букву сделайте прописной.
# Добавьте поле хеш на основе имени и идентификатора.
# Получившиеся записи сохраните в json файл, где каждая строка
# csv файла представлена как отдельный json словарь.
# Имя исходного и конечного файлов передавайте как аргументы
# функции.

import csv
import json
import pickle

def change_csv(file_csv: str):
    result = {}
    with open(file_csv, 'r', encoding='UTF-8') as file:
        data = file.readlines()
        for i, items in enumerate(data):
            data[i] = data[i].strip().split('|')
            data[i][0] = data[i][0].title()
            data[i][1] = data[i][1].zfill(10)
            result[hash(data[i][0] + data[i][1])] = data[i]
    return result


def from_csv_to_json(file_csv:str, file_json: str):
    result_dic = change_csv(file_csv)
    with open(file_json, 'w', encoding='utf-8') as file:
        json.dump(result_dic, file, indent = 4, ensure_ascii=False )

from_csv_to_json('../csv/user_data.csv', 'json/new_user_data.json')
with open('../json/new_user_data.json', 'r', encoding='UTF-8') as f:
    data = json.load(f)
    print(data)
with open('../pickle/task_6.pickle', 'wb') as f1:
     pickle.dump(data,f1)