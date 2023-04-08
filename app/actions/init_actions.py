import re
import os
import json

from app.actions.helper_actions import read_json, to_valid_exercise, build_id
from app.context.Mock import Mock
from app.context.ValidatorContext import ValidatorContext
from app.models.ExpectedExercise import ExpectedExercise


def _init_expected_exercises():
    expected_exercises = {}

    labs_expected_exercises = read_json('exercises.json')

    for i, lab in enumerate(labs_expected_exercises):
        for title, body in lab.items():
            expected_exercises[f"lab_{i+1}_{title}"] = ExpectedExercise(body["expected_outputs"],
                                                     body["plagiarism_quantity"],
                                                     body["process_input"])
    return expected_exercises


def _init_actual_exercises():
    actual_exercises = {}

    path_to_json_files = 'filesToCheck/'
    notebook_file_names = [filename for filename in os.listdir(path_to_json_files) if filename.endswith('.ipynb')]

    for notebook_file_name in notebook_file_names:
        cells = read_json('filesToCheck/{}'.format(notebook_file_name))['cells']

        for i in range(len(cells)):
            el = cells[i]

            if len(el['source']) <= 0:
                continue

            tmp = el['source'][0]

            results = re.findall("#+\s+Zadanie\s+[0-9]+\\n", tmp)

            if len(results) <= 0:
                continue

            title: str = "zadanie " + tmp[-2]
            content_lines: list[str] = cells[i + 1]['source']
            actual_exercises[(notebook_file_name, title)] = to_valid_exercise(title, content_lines, "random-creator", 0)

    return actual_exercises


def _init_mocks():
    mocks = []
    labs_expected_exercises = read_json('exercises.json')

    for i, lab in enumerate(labs_expected_exercises):
        for exercise_title, content in lab.items():
            data_series_list = content['data_series']

            for data_series_id, new_mocks in enumerate(data_series_list):
                print(f"{lab}_{i + 1}_{exercise_title}_{mocks}")

                for mock in new_mocks:
                    mocks.append(Mock(f"lab_{i+1}", exercise_title, mock['type'], mock['content'], data_series_id))

    return mocks


def init_context():
    expected_exercises = _init_expected_exercises()
    actual_exercises = _init_actual_exercises()
    mocks = _init_mocks()

    return ValidatorContext(expected_exercises, actual_exercises, mocks)


