from src.entities.question_answer import QuestionAnswer
from src.use_cases.ports.question_answer_port import QuestionAnswerPort


class ExamplesService:
    def __init__(self, examples_repository: QuestionAnswerPort):
        self.examples_repository = examples_repository
        self.scenario: QuestionAnswer = None

        self.examples: list[QuestionAnswer] = []
        """Fetch and manage examples from a JSON file."""

        self.excluded_keys = ["scenario"]
        """Keys of QuestionAnswer objects to exclude from specific use cases"""

        self.only_included: list[QuestionAnswer] = [
            ex for ex in self.examples if ex.key not in self.excluded_keys]
        """Subset of examples that are included in specific use cases"""

    @property
    def scenario_answer(self) -> str:
        return self.scenario.answer

    def get_examples(self, filepath: str):
        self.examples = self.examples_repository.load_json(filepath)
        self.only_included: list[QuestionAnswer] = [
            ex for ex in self.examples if ex.key not in self.excluded_keys]
        self.scenario = next(
            (ex for ex in self.examples if ex.key == 'scenario'), None)

    def list_included_question_answers(self) -> str:
        return self.examples_repository.create_question_answers(self.only_included)

    def create_included_question_answers(self) -> str:
        """
        Create a string of question answers from a list of the `only_included` 
        QuestionAnswer objects.
    
        Returns:
            dict: A dictionary of question answers.
        
        Example:
            Question:  What happened to make you want to give up?
            Answer: I just got stuck and stopped losing weight. In fact I gained a few pounds!
            Question: How did you feel emotionally at the time? 
            Answer: Terrible! I felt like all my efforts were pointless, and I started questioning if I could ever succeed in losing weight again.
            Question:  What was the worst part of this experience?
            Answer: It made me feel old - like I’d have to settle for being less healthy and attractive than I’d been when I was younger
            Question: How did the whole situation end? (did you give up? did you keep on going?)
            Answer: I almost gave up, but after the conversation with my friend, I decided to keep going and focus more on how I felt rather than just the numbers on the scale.
            Question: What do you think did or could have re-motivated your weight loss effort?
            Answer: Talking to a friend who reminded me that setbacks are normal and suggested focusing on how my clothes fit better and I have more energy.
        """
        return self.examples_repository.create_question_answers(self.examples)

    def create_key_answers(self) -> dict:
        """
        Create a dictionary of key answers from a list of all the `examples`
        QuestionAnswer objects.
    
        Returns:
            dict: A dictionary of key answers.
        
        Example:
            {
                "what" : "I just got stuck and stopped losing weight.  In fact I gained a few pounds!",
                "emotion": "Terrible! I felt like all my efforts were pointless, and I started questioning if I could ever succeed in losing weight again.",
                "worst": " It made me feel old - like I’d have to settle for being less healthy and attractive than I’d been when I was younger",
                "motivate": "Talking to a friend who reminded me that setbacks are normal and suggested focusing on how my clothes fit better and I have more energy.",
                "outcome": "I almost gave up, but after the conversation with my friend, I decided to keep going and focus more on how I felt rather than just the numbers on the scale.",
                "scenario": "I'd been putting a lot of effort into improving my diet and sticking to a regular exercise routine. After about a month of hard work, I was upset to see that I had actually gained a few pounds instead of losing them. This made me feel incredibly frustrated and hopeless, like all the effort I had put in was pointless. I began to doubt whether I could ever succeed in my weight loss journey. I was on the verge of giving up when I talked to a friend who reminded me that setbacks are a normal part of the process. They suggested that I focus on non-scale victories, like how my clothes were fitting better and I had more energy This conversation re-motivated me to keep going, and I decided to shift my focus from just the numbers on the scale to how I was feeling overall."
            }
        """
        return self.examples_repository.create_key_answers(self.examples)
