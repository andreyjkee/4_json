# -*- coding: utf-8 -*-
import json
from optparse import OptionParser


def load_data(filepath):
    if not filepath:
        raise Exception('Не указан путь к файлу')
    try:
        with open(filepath.strip(), 'r', encoding='utf-8') as f:
            return f.read()
    except FileNotFoundError:
        print('Файл : ', filepath, 'не найден')
    except Exception as e:
        print('Произошла ошибка', str(e))

def pretty_print_json(data):
    try:
        loaded_json = json.loads(data)
        print(json.dumps(sort_keys=True, indent=4, obj=loaded_json))
    except TypeError:
        print('Некорректный формат файла, файл должен содержать json структуру')


if __name__ == '__main__':
    parser = OptionParser()
    parser.add_option("-f", "--file", type="string", dest="filepath")
    (options, args) = parser.parse_args()
    content = load_data(options.filepath)
    if content:
        pretty_print_json(content)
