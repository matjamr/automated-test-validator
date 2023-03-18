from app.context.ValidatorContext import ValidatorContext
from app.executors.BaseExecutor import BaseExecutor


class ExercisesExecutor(BaseExecutor):

    def should_execute(self) -> bool:
        return False

    def execute(self, validator_context: ValidatorContext) -> None:
        for exercise_title, exercise in validator_context.actual_exercises.items():
            exercise.execute()
