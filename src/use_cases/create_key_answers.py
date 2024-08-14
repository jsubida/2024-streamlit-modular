from src.entities.question_answer import QuestionAnswer


def execute(questions: list[QuestionAnswer]) -> dict:
    """Create a dictionary of key answers based on a list of questions."""
    return {q.key: q.answer for q in questions}
