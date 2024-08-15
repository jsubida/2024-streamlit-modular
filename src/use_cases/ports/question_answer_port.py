import abc

from src.entities.question_answer import QuestionAnswer


class QuestionAnswerPort(abc.ABC):

    @abc.abstractmethod
    def create_key_answers(self, items) -> dict:
        pass

    @abc.abstractmethod
    def create_question_answers(self, items) -> str:
        pass

    @abc.abstractmethod
    def create_question_keys(self, items) -> str:
        pass

    @abc.abstractmethod
    def list_keys(self, items) -> str:
        pass

    @abc.abstractmethod
    def list_questions(self, items) -> str:
        pass
