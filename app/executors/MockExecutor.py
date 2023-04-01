from app.context.Mock import Mock
from app.context.ValidatorContext import ValidatorContext
from app.executors.BaseExecutor import BaseExecutor
from app.models.Exercise import Exercise
import re


class MockExecutor(BaseExecutor):

    def should_execute(self) -> bool:
        return True

    def execute(self, validator_context: ValidatorContext) -> None:

        exercises = validator_context.actual_exercises

        for exercise_title, exercise in exercises.items():
            mocks: list[Mock] = [mock for mock in validator_context.mocks if mock.exercise_title == exercise_title]

            new_content = exercise.content

            for mock in mocks:
                new_content = re.sub("{}\(input\(.+\)\)".format(mock.type), str(mock.content), new_content, 1)

            new_exercise = Exercise(exercise_title, new_content)

            exercises[exercise_title] = new_exercise
