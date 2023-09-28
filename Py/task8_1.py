# Вспоминаем задачу 3 из прошлого семинара. Мы сформировали
# текстовый файл с псевдо именами и произведением чисел.
# Напишите функцию, которая создаёт из созданного ранее
# файла новый с данными в формате JSON.
# Имена пишите с большой буквы.
# Каждую пару сохраняйте с новой строки.

import json
import os

with open(os.path.join('../..', 'sem7', 'text_1'), 'r', encoding='UTF-8') as f:
    lst = []
    for line in f:
        lst.append(tuple(line[:-3].split('|')))
with open('../json/json_f.json', 'w') as f1:
    json.dump(lst, f1, indent='\t')