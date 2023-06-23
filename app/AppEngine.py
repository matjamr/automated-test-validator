import logging

from app.actions.init_actions import init_context
from app.context.ValidatorContext import ValidatorContext
from app.executors.BaseExecutor import BaseExecutor
from app.executors.ExercisesExecutor import ExercisesExecutor
from app.executors.MockExecutor import MockExecutor
from app.executors.PlagiarismExecutor import PlagiarismExecutor
from app.executors.RaportExecutor import RaportExecutor


class AppEngine:

    def __init__(self):
        self.validator_context: ValidatorContext = init_context()

        self.executors: list[BaseExecutor] = [
            MockExecutor(),
            PlagiarismExecutor(),
            # ExercisesExecutor(),
            RaportExecutor()
        ]

    def start(self):
        logging.info("Starting processing...")

        for executor in self.executors:
            if executor.should_execute():
                logging.info("Executing....")
                executor.execute(self.validator_context)

