class ResultExercise:

    def __init__(self, lab_num: str, exercise_name: str, created_by: str, passed: bool, series_id: int):
        self.lab_num = lab_num
        self.exercise_name = exercise_name
        self.created_by = created_by
        self.passed = passed
        self.series_id = series_id

    def __str__(self) -> str:
        return "{} {} {} {}".format(self.lab_num, self.exercise_name, self.created_by, self.passed)