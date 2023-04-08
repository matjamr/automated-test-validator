class Mock:
    def __init__(self, lab_num: str, exercise_title: str, type: str, content: str, data_series_id: int):
        self.lab_num = lab_num
        self.type: str = type
        self.content: str = content
        self.exercise_title: str = exercise_title
        self.data_series_id = data_series_id

    def __str__(self):
        return "Mock [exercise_title={}, type={}, content={}]".format(self.exercise_title, self.type, self.content)
