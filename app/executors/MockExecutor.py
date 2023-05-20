import re

from app.context.Mock import Mock
from app.context.ValidatorContext import ValidatorContext
from app.executors.BaseExecutor import BaseExecutor


class MockExecutor(BaseExecutor):

    def should_execute(self) -> bool:
        return True

    def execute(self, validator_context: ValidatorContext) -> None:

        exercises = validator_context.actual_exercises

        for exercise_title, exercise in exercises.items():
            mocks: list[Mock] = [mock for mock in validator_context.mocks if mock.exercise_title == exercise_title[1] and mock.lab_num in exercise_title[0]]

            new_mocks_dict = self.split_mocks_into_series_dict(mocks)
            content_lists = []

            for data_series_id, mocks_list in new_mocks_dict.items():
                new_content = exercise.content

                for mock in mocks_list:
                    new_content = re.sub("{}\(input\(.+\)\)".format(mock.type), str(mock.content), new_content, 1)

                content_lists.append(new_content)

                # new_exercise = Exercise(exercise_title, con, exercise.creator, data_series_id)

            exercises[exercise_title].content_list = content_lists

    def split_mocks_into_series_dict(self, mocks) -> dict[int: list[Mock]]:
        find_max_id = max([mock.data_series_id for mock in mocks])
        new_mock_dict: dict[int: list[Mock]] = {}

        for id in range(find_max_id + 1):
            new_mock_dict[id] = [mock for mock in mocks if mock.data_series_id == id]

        return new_mock_dict
