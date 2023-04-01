import io
import sys
import traceback

from app.Assertions.Assertz import assert_that
from app.context.ValidatorContext import ValidatorContext
from app.executors.BaseExecutor import BaseExecutor


class ExercisesExecutor(BaseExecutor):

    def should_execute(self) -> bool:
        return True

    def execute(self, validator_context: ValidatorContext) -> None:
        for exercise_title, exercise in validator_context.actual_exercises.items():
            print("Checking {} validity".format(exercise_title))
            old_stdout = sys.stdout
            new_stdout = io.StringIO()
            sys.stdout = new_stdout

            exercise.execute()

            result = sys.stdout.getvalue().strip()
            sys.stdout = old_stdout

            self.validate(result, exercise_title, validator_context)

    def validate(self, result: str, exercise_title: str, validator_context: ValidatorContext):
        try:
            assert_that(result).is_equal_to(validator_context.expected_exercises[exercise_title].expected_output)
        except AssertionError as s:
            # print('\033[91m' + ''.join(traceback.format_tb(s.__traceback__)) + '\033[0m') -> custom assertion will
            # be thrown
            print("{} is not valid! :c".format(exercise_title))
        else:
            print("{} is valid! c:".format(exercise_title))
