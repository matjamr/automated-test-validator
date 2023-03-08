
import json


def read_json(filename: str) -> dict[str: object]:
    file = open(filename)
    data = json.load(file)
    file.close()

    return data

