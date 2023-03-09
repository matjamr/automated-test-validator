import json


def read_json(filename: str) -> dict[str: object]:
    with open(filename, 'r', encoding='utf-8') as file:
        data = json.load(file)
    return data

