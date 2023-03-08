import logging
import re

from app.Utils import read_json
from app.models.ExpectedExercise import ExpectedExercise


class AppEngine:

    def __init__(self):
        self.expected_exercises = {}
        self.actual_exercises = {}

    def start(self):
        logging.info("Starting processing...")

        for k, v in read_json('exercises.json').items():
            self.expected_exercises[k] = ExpectedExercise(v["expected_output"],
                                                          v["plagiarism_quantity"],
                                                          v["process_input"])

        cells = read_json('grzegorz.ipynb')['cells']

        print(cells)

        for i in range(len(cells)):
            el = cells[i]

            tmp = el['source'][0]

            results = re.findall("#+\s+Zadanie\s+[0-9]+\\n", tmp)

            if len(results) <= 0:
                continue

            self.actual_exercises["zadanie " + tmp[-2]] = cells[i + 1]['source']

        # print(self.actual_exercises)
        # program = ''.join(self.actual_exercises['zadanie 1'])
        # program = re.sub('float\(input\(.*\)\)', "2", program)
        # print(program)
        # exec(program, {'r': 11, 'R': 10})
