# TODO решите задачу
import json

INPUT_FILE = 'input.json'

def task() -> float:
    with open(INPUT_FILE, 'r', encoding='utf-8') as f:
        item = json.load(f)
    list_ = [i['score']*i['weight'] for i in item]
    return round(sum(list_), 3)


print(task())
