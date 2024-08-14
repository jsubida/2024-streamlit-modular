from src.entities.question_answer import QuestionAnswer
from src.use_cases.create_question_answers import execute


def test_execute_2_questions():
    # Arrange
    question_answers = [
        QuestionAnswer(question="What is your name?",
                       answer="My name is John"),
        QuestionAnswer(question="Where are you from?",
                       answer="I am from Chicago")
    ]

    # Act
    result = execute(question_answers)

    # Assert
    assert result == "Question: What is your name?\nAnswer: My name is John\nQuestion: Where are you from?\nAnswer: I am from Chicago"


def test_execute_0_questions():
    # Arrange
    question_answers = []

    # Act
    result = execute(question_answers)

    # Assert
    assert result == ""
