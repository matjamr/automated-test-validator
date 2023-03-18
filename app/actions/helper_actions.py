import json

from app.models.Exercise import Exercise


def read_json(filename: str) -> dict[str: object]:
    with open(filename, 'r', encoding='utf-8') as file:
        data = json.load(file)
    return data


def to_valid_exercise(title: str, exercise_lines: list[str]) -> Exercise:
    return Exercise(title, ''.join(exercise_lines))
