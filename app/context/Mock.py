class Mock:
    def __init__(self, exercise_title, type, content):
        self.type = type
        self.content = content
        self.exercise_title = exercise_title

    def __str__(self):
        return "Mock [exercise_title={}, type={}, content={}]".format(self.exercise_title, self.type, self.content)
