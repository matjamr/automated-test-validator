class Exercise:
    def __init__(self, title: str, content: str):
        self.title = title
        self.content = content

    def execute(self) -> str:
        return exec(self.content)

    def __str__(self):
        return "Exercise [title = {}, content = ...]".format(self.title)
