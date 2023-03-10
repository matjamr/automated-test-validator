import difflib
import json
import glob
import re


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
        task_names = []
        for keys, values in self.students_tasks.items():
            for key in values.keys():
                task_names.append(key)
            break

        for task in task_names:
            for i in range(len(students_names)):
                for j in range(i + 1, len(students_names)):
                    try:
                        differ = difflib.SequenceMatcher(None, self.students_tasks[students_names[i]][task],
                                                         self.students_tasks[students_names[j]][task])
                        similarity_ratio = differ.ratio()
                        if similarity_ratio > 0.7:
                            print(f"{students_names[i]} i {students_names[j]} {task} Podobienstwo: {similarity_ratio}")

                    except IndexError:
                        continue
