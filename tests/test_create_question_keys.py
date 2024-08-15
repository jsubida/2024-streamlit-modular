import pytest

from src.entities.question_answer import QuestionAnswer
from src.use_cases.create_question_keys import execute


def test_execute_returns_string():
    question_answers = [QuestionAnswer(
        "What is your name?", "John", "k1"), QuestionAnswer("What is your age?", "25", "k2")]
    result = execute(question_answers)
    assert isinstance(result, str)


def test_execute_returns_correct_number_of_keys():
    question_answers = [QuestionAnswer(
        "What is your name?", "John", "k1"), QuestionAnswer("What is your age?", "25", "k2")]
    result = execute(question_answers)
    assert len(result.split("\n")) == 2 * len(question_answers)


def test_execute_returns_empty_string_for_empty_input():
    question_answers = []
    result = execute(question_answers)
    assert result == ""
