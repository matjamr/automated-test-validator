import logging

from app.actions.init_actions import init_context
from app.context.ValidatorContext import ValidatorContext
from app.executors.BaseExecutor import BaseExecutor
from app.executors.ExercisesExecutor import ExercisesExecutor
from app.executors.MockExecutor import MockExecutor
from app.executors.PlagiarismExecutor import PlagiarismExecutor


class AppEngine:

    def __init__(self):
        self.validator_context: ValidatorContext = init_context()

        self.executors: [BaseExecutor] = [
            MockExecutor(),
            PlagiarismExecutor(),
            ExercisesExecutor()
        ]

    def start(self):
        logging.info("Starting processing...")

        for executor in self.executors:
            if executor.should_execute():
                logging.info("Executing....")
                executor.execute(self.validator_context)



        # print(self.actual_exercises)
        # program = ''.join(self.actual_exercises['zadanie 1'])
        # program = re.sub('float\(input\(.*\)\)', "2", program)
        # print(program)
        # exec(program, {'r': 11, 'R': 10})