import json

from src.entities.question_answer import QuestionAnswer
from src.entities.template import Template


def execute(filepath: str) -> Template:
    """Load template from a JSON file."""
    with open(filepath) as f:
        raw = json.load(f)
    raw["examples"] = [QuestionAnswer(**x) for x in raw["examples"]]
    return Template(**raw)
