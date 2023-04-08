class Exercise:
    def __init__(self, title: str, content: str, creator: str, test_data_series: int, content_list: list[str] = None):
        self.title = title
        self.content = content
        self.creator = creator
        self.test_data_series = test_data_series
        self.content_list = content_list

    def execute(self, data_series_id: int) -> str:
        return exec(self.content_list[data_series_id])

    def __str__(self):
        return "Exercise [title = {}, content = ...]".format(self.title)
