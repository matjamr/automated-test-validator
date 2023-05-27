from app.context import ValidatorContext
from app.executors.BaseExecutor import BaseExecutor

import pandas as pd

import xlsxwriter

from app.models.ResultExercise import ResultExercise


class RaportExecutor(BaseExecutor):

    def should_execute(self) -> bool:
        return True

    def execute(self, validator_context: ValidatorContext) -> None:

        # Create a workbook and add a worksheet.
        workbook = xlsxwriter.Workbook('Expenses01.xlsx')

        lab_dict: dict[str:list[ResultExercise]] = self.init_lab_dict(validator_context)

        for lab_num, exercises in lab_dict.items():
            worksheet = workbook.add_worksheet(lab_num)

            row = 1

            worksheet.write(0, 0, "Numer zadania")
            worksheet.write(0, 1, "kto to zrobil")
            worksheet.write(0, 2, "Czy przeszlo?")

            # Iterate over the data and write it out row by row.
            for exercise in exercises:
                worksheet.write(row, 0, exercise.exercise_name)
                worksheet.write(row, 1, exercise.created_by)
                worksheet.write(row, 2, exercise.passed)

                row += 1

        workbook.close()

    def init_lab_dict(self, validator_context: ValidatorContext) -> dict:

        lab_dict = {}

        for exercise in validator_context.exercises_result:
            lab_dict[exercise.lab_num] = []

        for exercise in validator_context.exercises_result:
            lab_dict[exercise.lab_num].append(exercise)

        return lab_dict
