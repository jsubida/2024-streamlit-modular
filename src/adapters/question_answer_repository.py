from src.use_cases import (
    create_key_answers,
    create_question_answers,
    create_question_keys,
    list_keys,
    list_questions,
)
from src.use_cases.ports.question_answer_port import QuestionAnswerPort


class QuestionAnswerRepository(QuestionAnswerPort):
    """A repository class that provides methods to interact with a QuestionAnswer objects."""

    def create_key_answers(self, items):
        return create_key_answers.execute(items)

    def create_question_answers(self, items):
        return create_question_answers.execute(items)

    def create_question_keys(self, items) -> str:
        return create_question_keys.execute(items)

    def list_keys(self, items):
        return list_keys.execute(items)

    def list_questions(self, items):
        return list_questions.execute(items)
