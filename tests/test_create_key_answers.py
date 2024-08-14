from src.entities.question_answer import QuestionAnswer
from src.use_cases.create_key_answers import execute


def test_execute_empty():
    # Test case 1: Empty list of questions
    questions = []
    expected_output = {}
    assert execute(questions) == expected_output


def test_execute_1_question():
    # Test case 2: Single question
    question = QuestionAnswer(
        "What is the capital of France?", "Paris", "fra_capital")
    questions = [question]
    expected_output = {"fra_capital": "Paris"}
    assert execute(questions) == expected_output


def test_execute_multiple_questions():
    # Test case 3: Multiple questions
    question1 = QuestionAnswer(
        "What is the capital of France?", "Paris", "fra_capital")
    question2 = QuestionAnswer(
        "What is the capital of Germany?", "Berlin", "ger_capital")
    question3 = QuestionAnswer(
        "What is the capital of Italy?", "Rome", "ita_capital")
    questions = [question1, question2, question3]
    expected_output = {
        "fra_capital": "Paris",
        "ger_capital": "Berlin",
        "ita_capital": "Rome"
    }
    assert execute(questions) == expected_output
