import json
from optparse import OptionParser


def load_data(filepath):
    if not filepath:
        raise Exception('Не указан путь к файлу')
    try:
        with open(filepath.strip(), 'r', encoding='utf-8') as f:
            return json.loads(f.read())
    except FileNotFoundError:
        print('Файл : ', filepath, 'не найден')

def pretty_print_json(data):
    try:
        print(json.dumps(sort_keys=True, indent=4, obj=data))
    except TypeError:
        print('Некорректный формат файла, файл должен содержать json структуру')


if __name__ == '__main__':
    parser = OptionParser()
    parser.add_option("-f", "--file", type="string", dest="filepath")
    (options, args) = parser.parse_args()
    content = load_data(options.filepath)
    if content:
        pretty_print_json(content)
