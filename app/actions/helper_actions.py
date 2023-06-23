import json
import glob
import re
from app.models.Exercise import Exercise
import os

def read_json(filename: str) -> dict[str: object]:
    with open(filename, 'r', encoding='utf-8') as file:
        data = json.load(file)
    return data


def to_valid_exercise(title: str, exercise_lines: list[str], creator: str, test_data_series: int, lab_num: str) -> Exercise:
    return Exercise(title, ''.join(exercise_lines), creator, test_data_series, [], "lab_" + lab_num)


def load_file() -> dict[str: object]:
    folder_path = 'lab/'
    ipynb_files = glob.glob(os.path.join(folder_path, '**/*.ipynb'), recursive=True)
    json_data = {}
    for file_path in ipynb_files:
        with open(file_path, 'r', encoding='utf-8') as file:
            notebook_content = file.read()
        notebook_json = json.loads(notebook_content)
        relative_path = os.path.relpath(file_path, folder_path)
        json_data[relative_path] = notebook_json['cells']

    return json_data


def download_tasks(json_data) -> dict[dict[str: object]]:
    number_task = 1
    students_tasks = {}

    for key, value in json_data.items():
        students_tasks[key] = {}

        for i in range(len(value)):
            el = value[i]
            tmp = ''.join(el['source'])
            results = re.findall("#+\s+Zadanie\s+[0-9]+\\n", tmp)

            if len(results) <= 0:
                continue

            students_tasks[key]["zadanie " + str(number_task)] = ''.join(value[i + 1]['source'])
            number_task += 1

        number_task = 1

    return students_tasks


def build_id(notebook_name, exercise_title):
    return f"{notebook_name}-{exercise_title}"
