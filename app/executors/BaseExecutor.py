from app.context.ValidatorContext import ValidatorContext


class BaseExecutor:
    def should_execute(self, ) -> bool:
        raise NotImplementedError

    def execute(self, validator_context: ValidatorContext) -> None:
        raise NotImplementedError
