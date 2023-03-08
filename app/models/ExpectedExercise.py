
class ExpectedExercise:

    def __init__(self, expected_output: str = 'NONE', plagiarism_quantity: str = 'NONE', process_input: bool = False):
        self.expected_output = expected_output
        self.plagiarism_quantity = plagiarism_quantity
        self.process_input = process_input

    def __str__(self) -> str:
        return "{} {} {}".format(self.expected_output, self.plagiarism_quantity, self.process_input)




