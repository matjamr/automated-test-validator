import difflib
import pandas as pd
import copydetect
import os
from app.actions.helper_actions import load_file, download_tasks


class CheckPlagiarism:
    def __init__(self):
        self.json_data = load_file()
        self.students_tasks = download_tasks(self.json_data)

    def start(self):
        students_names = list(self.students_tasks.keys())
        tasks_to_skip = import_tasks_to_skip(students_names[0])
        task_names = self.get_task_names(tasks_to_skip)

        for task in task_names:
            self.compare_students(task, students_names)

    def get_task_names(self, tasks_to_skip):
        task_names = []
        for values in self.students_tasks.values():
            for key in values.keys():
                if key not in tasks_to_skip:
                    task_names.append(key)
            break
        return task_names

    def compare_students(self, task, students_names):
        for i in range(len(students_names)):
            for j in range(i + 1, len(students_names)):
                try:
                    similarity_ratio = self.get_similarity_ratio(students_names, i, j, task)
                    if similarity_ratio > 0.85:
                        self.write_files(students_names, i, j, task)
                        similarity_score = get_similarity_score(students_names, i, j, task)
                        if similarity_score > 0.85:
                            print_result(students_names, i, j, task, similarity_ratio, similarity_score)
                            clean_up_files()

                except IndexError:
                    continue

    def get_similarity_ratio(self, students_names, i, j, task):
        differ = difflib.SequenceMatcher(None, self.students_tasks[students_names[i]][task],
                                         self.students_tasks[students_names[j]][task])
        return differ.ratio()

    def write_files(self, students_names, i, j, task):
        with open(f"result/{students_names[i]}_{task}.py", "a", encoding='utf-8') as file1:
            file1.write(f"{self.students_tasks[students_names[i]][task]}")
        with open(f"result/{students_names[j]}_{task}.py", "a", encoding='utf-8') as file2:
            file2.write(f"{self.students_tasks[students_names[j]][task]}")


def import_tasks_to_skip(lab_num: str):
    df = pd.read_excel("tasksToBeMissed/data.xlsx")
    # lab_num[-7] is laboratory number "name_laboratoryNumber.ipynb"
    return df[int(lab_num[-7])].tolist()


def get_similarity_score(students_names: list[str], i: int, j: int, task: str):
    file_path1 = f"result/{students_names[i]}_{task}.py"
    file_path2 = f"result/{students_names[j]}_{task}.py"
    fp1 = copydetect.CodeFingerprint(file_path1, 25, 1)
    fp2 = copydetect.CodeFingerprint(file_path2, 25, 1)
    token_overlap, similarities, _ = copydetect.compare_files(fp1, fp2)
    return similarities[0]


def print_result(students_names: list[str], i: int, j: int, task: str, similarity_ratio: float,
                 similarity_score: float) -> None:
    print(f"{students_names[i]} i {students_names[j]}\n{task} "
          f"\nTEST LEKSYKALNY: {similarity_ratio}"
          f"\nTEST \"MOSS\": {similarity_score}"
          f"\nTRZEBA SPRAWDZIC TO ZADANIE\n")


def clean_up_files() -> None:
    folder = 'result/'
    for filename in os.listdir(folder):
        file_path = os.path.join(folder, filename)
        if os.path.isfile(file_path):
            os.remove(file_path)
