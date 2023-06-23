from app.context import ValidatorContext
from app.executors.BaseExecutor import BaseExecutor

import xlsxwriter

from app.models.ResultExercise import ResultExercise


class RaportExecutor(BaseExecutor):

    def should_execute(self) -> bool:
        return True

    def execute(self, validator_context: ValidatorContext) -> None:

        # Create a workbook and add a worksheet.
        workbook = xlsxwriter.Workbook('Result.xlsx')

        lab_dict: dict[str:list[ResultExercise]] = self.init_lab_dict(validator_context)

        self.process_folders_status(validator_context, workbook)
        self.process_exercises(lab_dict, workbook)

        workbook.close()

    def process_exercises(self, lab_dict, workbook):
        for lab_num, exercises in lab_dict.items():
            worksheet = workbook.add_worksheet(lab_num)

            row = 1

            worksheet.write(0, 0, "Numer zadania")
            worksheet.write(0, 1, "kto to zrobil")
            worksheet.write(0, 2, "Czy przeszlo?")

            for exercise in exercises:
                worksheet.write(row, 0, exercise.exercise_name)
                worksheet.write(row, 1, exercise.created_by)
                worksheet.write(row, 2, exercise.passed)

                row += 1

    def process_folders_status(self, validator_context, workbook):
        worksheet = workbook.add_worksheet("STATUS")

        all_labs = list(dict.fromkeys([folder.lab_folder for folder in validator_context.folders_structure]))
        sorted(all_labs, reverse=True)

        for col, lab_num in enumerate(all_labs):
            worksheet.write(0, col + 1, lab_num)

        worksheet.write(0, len(all_labs) + 1, "przeslane/wszystkie")

        user_labs_dict = {}

        for folder in validator_context.folders_structure:

            if folder.name_surname + " " + folder.student_id not in user_labs_dict.keys():
                user_labs_dict[folder.name_surname + " " + folder.student_id] = [(folder.lab_folder, folder.is_ok)]
            else:
                user_labs_dict[folder.name_surname + " " + folder.student_id].append((folder.lab_folder, folder.is_ok))

        row = 1
        for name_surname_student_id, lab_arr in user_labs_dict.items():
            col = 1
            worksheet.write(row, 0, name_surname_student_id)
            for lab_tupl in lab_arr:
                worksheet.write(row, col, lab_tupl[0] + ":" + str(lab_tupl[1]))
                col += 1

            completed = sum([1 if lab_tupl[1] else 0 for lab_tupl in lab_arr])
            worksheet.write(row, col, f"{completed}/{len(lab_arr)}")

            row += 1


    def init_lab_dict(self, validator_context: ValidatorContext) -> dict:

        lab_dict = {}

        for exercise in validator_context.exercises_result:
            lab_dict[exercise.lab_num] = []

        for exercise in validator_context.exercises_result:
            lab_dict[exercise.lab_num].append(exercise)

        return lab_dict
