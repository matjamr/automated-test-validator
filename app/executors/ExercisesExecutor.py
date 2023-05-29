import io
import sys
import traceback

from app.Assertions.Assertz import assert_that
from app.context.ValidatorContext import ValidatorContext
from app.executors.BaseExecutor import BaseExecutor
from app.models.Exercise import Exercise
from app.models.ResultExercise import ResultExercise


class ExercisesExecutor(BaseExecutor):

    def should_execute(self) -> bool:
        return True

    def execute(self, validator_context: ValidatorContext) -> None:
        for lab_filename_exercise_title_tuple, exercise in validator_context.actual_exercises.items():

            if len(exercise.content_list) > 0:
                for series_id, content_exercise in enumerate(exercise.content_list):
                    self.exec(exercise, lab_filename_exercise_title_tuple, series_id, validator_context)
            else:
                self.exec(exercise, lab_filename_exercise_title_tuple, 0, validator_context)

    def exec(self, exercise, lab_filename_exercise_title_tuple, series_id, validator_context):
        print("Checking {} validity with data series: {}".format(lab_filename_exercise_title_tuple[1],
                                                                 series_id))

        id: str = self.tuple_to_exercise_id(lab_filename_exercise_title_tuple)

        try:

            old_stdout = sys.stdout
            new_stdout = io.StringIO()
            sys.stdout = new_stdout
            exercise.execute(series_id)
            result = sys.stdout.getvalue().strip()
            sys.stdout = old_stdout

            assert_that(result).is_equal_to(validator_context.expected_exercises[id].expected_outputs[series_id])

        except Exception as s:
            print("{} is not valid! :c FOR {}".format(lab_filename_exercise_title_tuple, series_id))

            validator_context.exercises_result.append(ResultExercise(exercise.lab_num,
                                                                     lab_filename_exercise_title_tuple[1],
                                                                     exercise.creator, False, id))

        else:
            print("{} is valid! c: FOR {}".format(lab_filename_exercise_title_tuple, series_id))

            validator_context.exercises_result.append(ResultExercise(exercise.lab_num,
                                                                     lab_filename_exercise_title_tuple[1],
                                                                     exercise.creator, True, id))

    def tuple_to_exercise_id(self, tupl):
        arr = tupl[0].split("_")[:2]

        print(tupl)

        return f"{'_'.join(arr)}_{tupl[1]}"
