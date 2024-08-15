from src.entities.template import Template
from src.use_cases import load_json
from src.use_cases.ports.template_port import TemplatePort


class TemplateRepository(TemplatePort):
    """A repository class that provides methods to interact with a Template object."""

    def __init__(self):
        pass

    def load_template(self, filepath: str) -> Template:
        return load_json.execute(filepath)
