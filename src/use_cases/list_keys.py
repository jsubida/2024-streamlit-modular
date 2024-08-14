from src.entities.question_answer import QuestionAnswer


def execute(questions: list[QuestionAnswer]) -> str:
    """List the keys of the questions in a comma separated string."""
    return ','.join([question.key for question in questions])
