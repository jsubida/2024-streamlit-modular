from src.entities.template import Template
from src.use_cases.ports.question_answer_port import QuestionAnswerPort
from src.use_cases.ports.template_port import TemplatePort


class TemplateService:
    """A service class that provides methods to interact with a Template object."""

    def __init__(self, template_repository: TemplatePort, question_answer_repository: QuestionAnswerPort):
        self.template_repository = template_repository
        self.question_answer_repository = question_answer_repository
        self.template: Template = None

    @property
    def interest(self) -> str:
        return self.template.conversation_interest

    @property
    def project_name(self) -> str:
        return self.template.id

    @property
    def prompt_keys(self) -> list[str]:
        return [prompt.key for prompt in self.template.examples]

    @property
    def prompt_datacollection(self) -> str:
        return f"""
        You're a community worker who is collecting stories from adults across a range of racial/ethnic backgrounds who have (or had) overweight/obesity to learn about their experiences trying to lose weight. In this conversation, {self.interest}.

        Your goal is to gather structured answers to the following questions.

        {self.list_questions()}

        Ask each question one at a time, using empathetic and adult friendly language while maintaining a descriptive tone. Do not include '-' when you ask the question.  Ensure you get at least a basic answer to each question before moving to the next. Never answer for the human. If you are unsure what the human meant, ask again.

        Once you have collected answers to all four questions, stop the conversation and write a single word "FINISHED"

        Current conversation:
        {{history}}
        Human: {{input}}
        AI:
        """

    @property
    def prompt_adaptation(self) -> str:
        return f"""
        You're a helpful assistant, helping patients adapt a scenario to their liking. The original scenario this student came with:

        Scenario: {self.scenario}.

        Their current request is {{input}}.

        Suggest an alternative version of the scenario. Keep the language and content as similar as possible, while fulfiling the patient's request.

        Return your answer as a JSON file with a single entry called 'new_scenario'

        """

    @property
    def prompt_one_shot(self) -> str:
        return f"""
        {{main_prompt}}

        Example:
        {self.create_question_answers()}

        The scenario based on these responses: {self.scenario}

        Your task:
        Create scenario based on the following answers:
        {self.create_question_keys()}


        {{end_prompt}}
        Your output should be a JSON file with a single entry called 'output_scenario'

        """

    @property
    def end_prompt_core(self) -> str:
        return "Create a scenario based on these responses, using adult friendly language."

    @property
    def extraction_prompt(self) -> str:
        return f"""
        You are an expert extraction algorithm.
        Only extract relevant information from the Human answers in the text.
        Use only the words and phrases that the text contains.
        If you do not know the value of an attribute asked to extract,
        return null for the attribute's value.

        You will output a JSON with {self.list_keys()} keys.

        These correspond to the following questions

        {self.list_questions()}

        Message to date: {{conversation_history}}

        Remember, only extract text that is in the messages above and do not change it.
        """

    @property
    def scenario(self) -> str:
        return self.template.scenario

    def create_key_answers(self) -> dict:
        """
        Create a dictionary of key answers from a list of all the `template.examples`
        QuestionAnswer objects. Include the scenario.
    
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
        val = self.question_answer_repository.create_key_answers(
            self.template.examples)
        val["scenario"] = self.scenario
        return val

    def create_question_answers(self) -> str:
        """
        Create a string of question answers from a list of the `template.examples` 
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
        return self.question_answer_repository.create_question_answers(
            self.template.examples)

    def create_question_keys(self) -> str:
        """Create a string of question and answer pairs based on a list of questions.
    
        Example:
            Question:  What happened to make you want to give up?
            Answer: {what}
            Question:How did you feel emotionally at the time? 
            Answer: {emotion}
            Question:  What was the worst part of this experience?
            Answer: {worst}
            Question: How did the whole situation end? (did you give up? did you keep on going?)
            Answer: {outcome}
            Question: What do you think did or could have re-motivated your weight loss effort?
            Answer: {motivate}
        """
        return self.question_answer_repository.create_question_keys(
            self.template.examples)

    def get_template(self, filepath: str):
        self.template = self.template_repository.load_template(filepath)

    def list_keys(self) -> str:
        """List the keys of the questions in a comma separated string."""
        return self.question_answer_repository.list_keys(
            self.template.examples)

    def list_questions(self) -> str:
        """List the questions in a formatted string.
    
        Example:
            - What happened to make you want to give up?
            - How did you feel emotionally at the time? 
            - What was the worst part of this experience?
            - How did the whole situation end? (did you give up? did you keep on going?)
            - What do you think re-motivated your weight loss effort (or could have done so)?
        """
        return self.question_answer_repository.list_questions(
            self.template.examples)
