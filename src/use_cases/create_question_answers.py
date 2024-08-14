from src.entities.question_answer import QuestionAnswer


def execute(question_answers: list[QuestionAnswer]) -> str:
    return "\n".join([f"Question: {qa.question}\nAnswer: {qa.answer}" for qa in question_answers])
