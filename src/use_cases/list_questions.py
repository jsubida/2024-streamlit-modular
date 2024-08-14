from src.entities.question_answer import QuestionAnswer


def execute(questions: list[QuestionAnswer]) -> str:
    """List the questions in a formatted string."""
    return "\n".join([f"- {q.question}" for q in questions])
