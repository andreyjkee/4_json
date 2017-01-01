import json
import os
from json.decoder import JSONDecodeError
from optparse import OptionParser


def load_data(filepath):
    if not filepath:
        raise Exception('Не указан путь к файлу')
    if not os.path.exists(filepath):
        raise FileNotFoundError({'message': 'Файл {0} не найден'.format(filepath)})
    with open(filepath.strip(), 'r', encoding='utf-8') as f:
        try:
            return json.loads(f.read())
        except JSONDecodeError:
            print('Файл {0} содержит отличную от JSON структуру'.format(filepath))

def pretty_print_json(data):
    print(json.dumps(sort_keys=True, indent=4, obj=data))


if __name__ == '__main__':
    parser = OptionParser()
    parser.add_option("-f", "--file", type="string", dest="filepath")
    (options, args) = parser.parse_args()
    content = load_data(options.filepath)
    if content:
        pretty_print_json(content)
