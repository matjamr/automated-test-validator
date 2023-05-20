from app.context.Mock import Mock


class ValidatorContext:

    def __init__(self, expected_exercises={}, actual_exercises={}, mocks: list[Mock]=[], exercises_result: list=[]):
        self.expected_exercises = expected_exercises
        self.actual_exercises = actual_exercises
        self.mocks = mocks
        self.exercises_result = exercises_result

