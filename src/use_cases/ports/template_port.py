import abc

from src.entities.template import Template


class TemplatePort(abc.ABC):
    """Port to interact with the Template entity"""

    @abc.abstractmethod
    def load_template(self, filepath: str) -> Template:
        pass
