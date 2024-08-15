from dataclasses import dataclass

from src.entities.question_answer import QuestionAnswer


@dataclass
class Template:
    id: str
    """The id of the template"""

    conversation_interest: str
    """The topic of interest for the conversation"""

    scenario: str
    """The scenario to be adapted"""

    examples: list[QuestionAnswer]
    """The examples to be used in the prompt"""
