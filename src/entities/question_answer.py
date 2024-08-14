from dataclasses import dataclass


@dataclass
class QuestionAnswer:
    question: str
    answer: str
    key: str = ""
