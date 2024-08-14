import json

from src.entities.question_answer import QuestionAnswer


def execute(filepath: str) -> list[QuestionAnswer]:
    """Load questions from a JSON file."""
    with open(filepath) as f:
        questions = json.load(f)
    return [QuestionAnswer(**q) for q in questions]
