# Напишите функцию, которая ищет json файлы в указанной
# директории и сохраняет их содержимое в виде
# одноимённых pickle файлов.
import json
import pickle
from pathlib import Path
import pickle
def json_to_pickle():
    paths = (Path('..').glob(f'*.json'))
    names = list(map(str, paths))
    for name in names:
        with open(name, 'r', encoding='utf-8') as file:
            j_file = json.load(file)
            with open(f'{name.split(".")[0]}.picle', 'wb') as file1:
                pickle.dump(j_file,file1)




json_to_pickle()