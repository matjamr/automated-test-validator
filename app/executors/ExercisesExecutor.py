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

            for series_id, content_exercise in enumerate(exercise.content_list):
                print("Checking {} validity with data series: {}".format(lab_filename_exercise_title_tuple[1],
                                                                         series_id))

                old_stdout = sys.stdout
                new_stdout = io.StringIO()
                sys.stdout = new_stdout

                exercise.execute(series_id)

                result = sys.stdout.getvalue().strip()
                sys.stdout = old_stdout

                self.validate(result, lab_filename_exercise_title_tuple, validator_context, series_id, exercise)

        print("Dupoa dupa dupcia")

    def validate(self, result: str, lab_filename_exercise_title_tuple: tuple,
                 validator_context: ValidatorContext, series_id: int, exercise: Exercise):

        id: str = self.tuple_to_exercise_id(lab_filename_exercise_title_tuple)

        try:
            assert_that(result).is_equal_to(validator_context.expected_exercises[id].expected_outputs[series_id])

        except AssertionError as s:
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

        return f"{'_'.join(arr)}_{tupl[1]}"
