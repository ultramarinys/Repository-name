# TODO решите задачу
import json

INPUT_FILE = 'input.json'

def task() -> float:
    with open(INPUT_FILE, 'r', encoding='utf-8') as f:
        data = json.load(f)
    list_ = [float(i['score'])*float(i['weight']) for i in data]
    return round(sum(list_), 3)


print(task())
