import pytest

from src.entities.question_answer import QuestionAnswer
from src.use_cases.list_questions import execute


def test_execute_returns_empty_string_when_questions_list_is_empty():
    questions = []
    result = execute(questions)
    assert result == ""


def test_execute_returns_formatted_questions_when_questions_list_is_not_empty():
    questions = [
        QuestionAnswer("What is your name?", "My name is John."),
        QuestionAnswer("What is your age?", "I am 25 years old.")
    ]
    result = execute(questions)
    expected_result = "- What is your name?\n- What is your age?"
    assert result == expected_result, result
