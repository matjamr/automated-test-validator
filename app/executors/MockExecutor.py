from app.context.ValidatorContext import ValidatorContext
from app.executors.BaseExecutor import BaseExecutor


class MockExecutor(BaseExecutor):

    def should_execute(self) -> bool:
        return True

    def execute(self, validator_context: ValidatorContext) -> None:
        for exercise_title, exercise in validator_context.actual_exercises.items():
            stubs = [mock for mock in validator_context.mocks if mock.exercise_title == exercise_title]
            print(stubs)
