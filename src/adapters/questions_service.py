from src.entities.question_answer import QuestionAnswer
from src.use_cases.ports.question_answer_port import QuestionAnswerPort


class QuestionsService:
    """Fetch and manage prompts from a JSON file. Save answers to prompts."""

    def __init__(self, prompts_repository: QuestionAnswerPort):
        self.prompts_repository = prompts_repository
        self.prompts: list[QuestionAnswer] = []

    @property
    def prompt_keys(self) -> list[str]:
        return [prompt.key for prompt in self.prompts]

    def get_prompts(self, filepath: str):
        self.prompts = self.prompts_repository.load_json(filepath)

    def create_question_keys(self) -> str:
        return self.prompts_repository.create_question_keys(self.prompts)

    def list_questions(self) -> str:
        return self.prompts_repository.list_questions(self.prompts)

    def list_keys(self) -> str:
        return self.prompts_repository.list_keys(self.prompts)
