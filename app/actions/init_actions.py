import re

from app.actions.helper_actions import read_json, to_valid_exercise
from app.context.Mock import Mock
from app.context.ValidatorContext import ValidatorContext
from app.models.ExpectedExercise import ExpectedExercise


def _init_expected_exercises():
    expected_exercises = {}

    for k, v in read_json('exercises.json').items():
        expected_exercises[k] = ExpectedExercise(v["expected_output"],
                                                 v["plagiarism_quantity"],
                                                 v["process_input"])
    return expected_exercises


def _init_actual_exercises():
    actual_exercises = {}

    cells = read_json('filesToCheck/grzegorz1.ipynb')['cells']

    for i in range(len(cells)):
        el = cells[i]

        tmp = el['source'][0]

        results = re.findall("#+\s+Zadanie\s+[0-9]+\\n", tmp)

        if len(results) <= 0:
            continue

        title: str = "zadanie " + tmp[-2]
        content_lines: list[str] = cells[i + 1]['source']

        actual_exercises[title] = to_valid_exercise(title, content_lines)

    return actual_exercises


def _init_mocks():
    mocks = []

    for exercise_title, content in read_json('exercises.json').items():
        mocks_json = content['mocks']

        for mock in mocks_json:
            mocks.append(Mock(exercise_title, mock['type'], mock['content']))

    return mocks


def init_context():
    expected_exercises = _init_expected_exercises()
    actual_exercises = _init_actual_exercises()
    mocks = _init_mocks()

    return ValidatorContext(expected_exercises, actual_exercises, mocks)


