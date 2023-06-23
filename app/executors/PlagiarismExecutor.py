from app.context.ValidatorContext import ValidatorContext
from app.executors.BaseExecutor import BaseExecutor
from app.actions.helper_actions import load_file, download_tasks
import difflib
import pandas as pd
import copydetect
import os
from openpyxl import Workbook

TEST_1 = 0.95
TEST_2 = 0.95


class PlagiarismExecutor(BaseExecutor):
    def __init__(self):
        self.results = {
            'lab1': {
                'Student_1': [],
                'Student_2': [],
                'Numer_zad': [],
                'Test_1:': [],
                'Test_2:': [],
                'Czy_plagiat': []
            },
            'lab2': {
                'Student_1': [],
                'Student_2': [],
                'Numer_zad': [],
                'Test_1:': [],
                'Test_2:': [],
                'Czy_plagiat': []
            },
            'lab3': {
                'Student_1': [],
                'Student_2': [],
                'Numer_zad': [],
                'Test_1:': [],
                'Test_2:': [],
                'Czy_plagiat': []
            },
            'lab4': {
                'Student_1': [],
                'Student_2': [],
                'Numer_zad': [],
                'Test_1:': [],
                'Test_2:': [],
                'Czy_plagiat': []
            },
            'lab5': {
                'Student_1': [],
                'Student_2': [],
                'Numer_zad': [],
                'Test_1:': [],
                'Test_2:': [],
                'Czy_plagiat': []
            },
            'lab6': {
                'Student_1': [],
                'Student_2': [],
                'Numer_zad': [],
                'Test_1:': [],
                'Test_2:': [],
                'Czy_plagiat': []
            },
            'lab7': {
                'Student_1': [],
                'Student_2': [],
                'Numer_zad': [],
                'Test_1:': [],
                'Test_2:': [],
                'Czy_plagiat': []
            },
            'lab8': {
                'Student_1': [],
                'Student_2': [],
                'Numer_zad': [],
                'Test_1:': [],
                'Test_2:': [],
                'Czy_plagiat': []
            }
        }
        self.json_data = load_file()
        self.students_tasks = download_tasks(self.json_data)

    def should_execute(self) -> bool:
        return True

    def execute(self, validator_context: ValidatorContext) -> None:

        students_names = list(self.students_tasks.keys())

        task_names = self.get_task_names()

        for task in task_names:
            self.compare_students(task, students_names)

        self.write_result()

    def get_task_names(self) -> list[str]:
        task_names = []
        for values in self.students_tasks.values():
            for key in values.keys():
                task_names.append(key)
            break
        return task_names

    def compare_students(self, task: str, students_names) -> None:
        for i in range(len(students_names)):
            for j in range(i + 1, len(students_names)):
                try:
                    similarity_ratio = self.get_similarity_ratio(students_names, i, j, task)
                    if similarity_ratio >= TEST_1:
                        self.write_files(students_names, i, j, task)
                        similarity_score = get_similarity_score(students_names, i, j, task)
                        if similarity_score >= TEST_2:
                            self.update_result(students_names, i, j, task, similarity_ratio, similarity_score)
                            clean_up_files()

                except (IndexError, KeyError):
                    continue

    def get_similarity_ratio(self, students_names: list[int], i: int, j: int, task: str) -> float:
        differ = difflib.SequenceMatcher(None, self.students_tasks[students_names[i]][task],
                                         self.students_tasks[students_names[j]][task])
        return differ.ratio()

    def write_files(self, students_names: list[int], i: int, j: int, task: str) -> None:
        student_1 = students_names[i].split("\\")[1]
        lab_nr = students_names[i].split("\\")[0]
        student_2 = students_names[j].split("\\")[1]

        with open(f"result\{lab_nr}_{student_1}_{task}.py", "a", encoding='utf-8') as file1:
            file1.write(f"{self.students_tasks[students_names[i]][task]}")
        with open(f"result\{lab_nr}_{student_2}_{task}.py", "a", encoding='utf-8') as file2:
            file2.write(f"{self.students_tasks[students_names[j]][task]}")

    def update_result(self, students_names: list[str], i: int, j: int, task: str, test_1: float, test_2: float) -> None:
        lab_nr = students_names[i].split("\\")[0]
        student_1 = os.path.basename(students_names[i])
        student_2 = os.path.basename(students_names[j])
        self.results[lab_nr]['Student_1'].append(student_1)
        self.results[lab_nr]['Student_2'].append(student_2)
        self.results[lab_nr]['Numer_zad'].append(task)
        self.results[lab_nr]['Czy_plagiat'].append('tak')
        self.results[lab_nr]['Test_1:'].append(test_1)
        self.results[lab_nr]['Test_2:'].append(test_2)

    def write_result(self) -> None:
        wb = Workbook()
        for lab, lab_data in self.results.items():
            # Tworzenie nowego arkusza o nazwie 'lab_X'
            ws = wb.create_sheet(lab[0:5])

            # Sprawdzanie maksymalnej liczby wierszy w danych
            max_rows = max(len(value) for value in lab_data.values())

            # Tworzenie listy kolumn
            columns = list(lab_data.keys())

            # Dodawanie nagłówków kolumn
            ws.append(columns)

            # Dodawanie danych do arkusza
            for i in range(max_rows):
                row = [lab_data[column][i] if i < len(lab_data[column]) else None for column in columns]
                ws.append(row)

        # Usuwanie domyślnego arkusza
        default_sheet = wb['Sheet']
        wb.remove(default_sheet)

        # Zapisywanie pliku Excel
        wb.save('Plagiaty.xlsx')


def get_similarity_score(students_names: list[str], i: int, j: int, task: str) -> float:
    student_1 = students_names[i].split("\\")[1]
    lab_nr = students_names[i].split("\\")[0]
    student_2 = students_names[j].split("\\")[1]

    file_path1 = f"result\{lab_nr}_{student_1}_{task}.py"
    file_path2 = f"result\{lab_nr}_{student_2}_{task}.py"
    fp1 = copydetect.CodeFingerprint(file_path1, 25, 1)
    fp2 = copydetect.CodeFingerprint(file_path2, 25, 1)
    token_overlap, similarities, _ = copydetect.compare_files(fp1, fp2)
    return similarities[0]


def clean_up_files() -> None:
    folder = "result\\"
    for filename in os.listdir(folder):
        file_path = os.path.join(folder, filename)
        if os.path.isfile(file_path):
            os.remove(file_path)

# def import_tasks_to_skip(lab_num: str) -> list[str]:
#     df = pd.read_excel("tasksToBeMissed/data.xlsx")
#     # lab_num[4] is laboratory number "name_laboratoryNumber.ipynb"
#     return df[int(lab_num[4])].tolist()
