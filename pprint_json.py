import json
import os

def load_data(filepath):
    if not os.path.exists(filepath):
        return None
    with open(filepath,'r', encoding='utf-8') as json_file:
        return json.load(json_file)


def pretty_print_json(data):
	return json.dumps(data, indent=4,ensure_ascii=False)


if __name__ == '__main__':
    filepath = input("Введите путь к файлу: ")
    shops = load_data(filepath)
    
    if shops is None:
        print("Файла или папки с таким названием не существует.")
    else:
        print(pretty_print_json(shops))