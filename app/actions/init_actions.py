import re
import os
import json

from app.actions.helper_actions import read_json, to_valid_exercise, build_id
from app.context.Mock import Mock
from app.context.ValidatorContext import ValidatorContext
from app.models.FolderStructure import FolderStructure
from app.models.ExpectedExercise import ExpectedExercise


def _init_expected_exercises():
    expected_exercises = {}

    labs_expected_exercises = read_json('exercises.json')

    for i, lab in enumerate(labs_expected_exercises):
        for title, body in labs_expected_exercises[lab].items():
            expected_exercises[f"{lab}_{title}"] = ExpectedExercise(body["expected_outputs"],
                                                                    body["plagiarism_quantity"],
                                                                    body["process_input"])
    return expected_exercises


def _process_empty_student(name_surname, student_id, lab_folder):
    return FolderStructure(name_surname, student_id, lab_folder, False)


def _process_valid_student(actual_exercises, name_surname, student_id, lab_folder, notebook_path):
    cells = read_json(notebook_path)['cells']

    for i in range(len(cells)):
        el = cells[i]

        if len(el['source']) <= 0:
            continue

        tmp = el['source'][0]

        results = re.findall("#+\s+Zadanie\s+[0-9]+\\n", tmp)

        if len(results) <= 0:
            continue

        title: str = "zadanie " + tmp.split(" ")[-1][:-1]
        content_lines: list[str] = cells[i + 1]['source']
        actual_exercises[(notebook_path, title)] = to_valid_exercise(title, content_lines,
                                                                     name_surname, 0,
                                                                     lab_folder)  # [0] -> regex findall


def _init_new_way():
    path_to_json_files = 'lab/'
    folders = os.listdir(path_to_json_files)
    actual_exercises = {}
    student_folders = []

    for lab_folder in folders:

        current_lab_folder_name = os.listdir(path_to_json_files + lab_folder)

        for student_lab in current_lab_folder_name:
            name_surname = student_lab.split("_")[0]
            student_id = student_lab.split("_")[1]

            notebook_student_folder = os.listdir(path_to_json_files + lab_folder + "/" + student_lab)

            if len(notebook_student_folder) < 1:
               student_folders.append(FolderStructure(name_surname, student_id, lab_folder, False))
            else:
                student_folders.append(FolderStructure(name_surname, student_id, lab_folder, True))
                _process_valid_student(actual_exercises, name_surname, student_id, lab_folder,
                                       path_to_json_files + lab_folder + "/" + student_lab + "/" + notebook_student_folder[0])

    return actual_exercises, student_folders


def _init_mocks():
    mocks = []
    labs_expected_exercises = read_json('exercises.json')

    for i, lab in enumerate(labs_expected_exercises):
        for exercise_title, content in labs_expected_exercises[lab].items():
            data_series_list = content['data_series']

            for data_series_id, new_mocks in enumerate(data_series_list):
                print(f"{lab}_{i + 1}_{exercise_title}_{mocks}")

                for mock in new_mocks:
                    mocks.append(Mock(f"lab_{i + 1}", exercise_title, mock['type'], mock['content'], data_series_id))

    return mocks


def init_context():
    expected_exercises = _init_expected_exercises()
    mocks = _init_mocks()

    actual_exercises2, empty_folders = _init_new_way()

    return ValidatorContext(expected_exercises, actual_exercises2, mocks, empty_folders)