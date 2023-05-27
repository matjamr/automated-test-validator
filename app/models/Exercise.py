class Exercise:
    def __init__(self, title: str, content: str, creator: str, test_data_series: int, content_list: list[str] = None, lab_num: str = None):
        self.title = title
        self.content = content
        self.creator = creator
        self.test_data_series = test_data_series
        self.content_list = content_list
        self.lab_num = lab_num

    def execute(self, data_series_id: int) -> str:
        return exec(self.content_list[data_series_id])

    def __str__(self):
        return "Exercise [lab_num = {} title = {}, content = ...]".format(self.lab_num, self.title)
