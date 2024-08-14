from src.entities.question_answer import QuestionAnswer
from src.use_cases.list_keys import execute


def test_execute():
    # Create a list of QuestionAnswer objects for testing
    questions = [
        QuestionAnswer(key='key1', question='question1', answer='answer1'),
        QuestionAnswer(key='key2', question='question2', answer='answer2'),
        QuestionAnswer(key='key3', question='question3', answer='answer3')
    ]

    # Call the execute function with the test data
    result = execute(questions)

    # Check if the result is as expected
    assert result == 'key1,key2,key3'
