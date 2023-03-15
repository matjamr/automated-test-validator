import difflib
import json
import glob
import re
import pandas as pd
import copydetect
import os

# TODO[GRZEGORZ]: WIECEJ SKIPOW ZADAN W LAB1, GDY DOSTANE PLIKI DO INNYCH LAB

# TODO[Grzegorz]: zrobic testy na wiekszych ilosciach danych i kolejnych labolatoriow
# TODO[Grzegorz]: sprawdzic jak ratio wychodzi na plagiacie, ktory byl lekko refactorowany (zmienne, printy)
# TODO[Grzegorz]: rodzielic te klase na CheckPlagiarsim, loadFile, GenerateReport
# TODO[Grzegorz]: przeniesc klase ChcekPlagiarism do app


def import_tasks_to_skip(lab_num):
    df = pd.read_excel("tasksToBeMissed/data.xlsx")
    return df[int(lab_num[-7])].tolist()


class CheckPlagiarism:
    def __init__(self):
        self.json_data = None
        self.students_tasks = {}

    def load_file(self):
        folder_path = 'filesToCheck/'
        ipynb_files = glob.glob(folder_path + '*.ipynb')

        self.json_data = {}
        for file_path in ipynb_files:
            with open(file_path, 'r', encoding='utf-8') as file:
                notebook_content = file.read()
            notebook_json = json.loads(notebook_content)
            self.json_data[file_path[13::]] = notebook_json['cells']

    def download_tasks(self):
        number_task = 1

        for key, value in self.json_data.items():
            self.students_tasks[key] = {}

            for i in range(len(value)):
                el = value[i]
                tmp = ''.join(el['source'])
                results = re.findall("#+\s+Zadanie\s+[0-9]+\\n", tmp)

                if len(results) <= 0:
                    continue

                self.students_tasks[key]["zadanie " + str(number_task)] = ''.join(value[i + 1]['source'])
                number_task += 1

            number_task = 1

    def task_comparison(self):
        students_names = list(self.students_tasks.keys())
        tasks_to_skip = import_tasks_to_skip(students_names[0])
        task_names = []

        for keys, values in self.students_tasks.items():
            for key in values.keys():
                if key in tasks_to_skip:
                    continue
                else:
                    task_names.append(key)
            break

        # TODO[Grzegorz] : zmniejszyc Notacja dużego O, priorytet - niski  (bo mi sie nie chce myslec)
        for task in task_names:
            for i in range(len(students_names)):
                for j in range(i + 1, len(students_names)):
                    try:
                        differ = difflib.SequenceMatcher(None, self.students_tasks[students_names[i]][task],
                                                         self.students_tasks[students_names[j]][task])
                        similarity_ratio = differ.ratio()
                        if similarity_ratio > 0.85:
                            # print(f"{students_names[i]} i {students_names[j]} {task} Podobienstwo: {similarity_ratio}")

                            file1 = open(f"result/{students_names[i]}_{task}.py", "a", encoding='utf-8')
                            file2 = open(f"result/{students_names[j]}_{task}.py", "a", encoding='utf-8')
                            file1.write(f"{self.students_tasks[students_names[i]][task]}")
                            file2.write(f"{self.students_tasks[students_names[j]][task]}")
                            file1.close()
                            file2.close()

                            file_path1 = f"result/{students_names[i]}_{task}.py"
                            file_path2 = f"result/{students_names[j]}_{task}.py"

                            fp1 = copydetect.CodeFingerprint(file_path1, 25, 1)
                            fp2 = copydetect.CodeFingerprint(file_path2, 25, 1)

                            token_overlap, similarities, _ = copydetect.compare_files(fp1, fp2)
                            similarity_score = similarities[0]

                            folder = 'result/'
                            for filename in os.listdir(folder):
                                file_path = os.path.join(folder, filename)
                                if os.path.isfile(file_path):
                                    os.remove(file_path)

                            if similarity_score > 0.85:
                                print(f"{students_names[i]} i {students_names[j]} {task} "
                                      f"TEST LEKSYKALNY: {similarity_ratio}"
                                      f" TEST \"MOSS\": {similarity_score}")

                    except IndexError:
                        continue

    def generate_report(self, student_a, student_b, task_number, similarity):
        # TODO[Grzegorz]: dodac generowanie raportow (w nowej klasie)
        pass
