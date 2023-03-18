from app.context.ValidatorContext import ValidatorContext
from app.executors.BaseExecutor import BaseExecutor


class PlagiarismExecutor(BaseExecutor):

    def should_execute(self) -> bool:
        return False

    def execute(self, validator_context: ValidatorContext) -> None:
        pass