from src.adapters.examples_service import ExamplesService
from src.adapters.question_answer_repository import QuestionAnswerRepository
from src.adapters.questions_service import QuestionsService

repo = QuestionAnswerRepository()
questions_service = QuestionsService(repo)
questions_service.get_prompts("./resources/questions1.json")

prompt_datacollection = """
You're a community worker who is collecting stories from adults across a range of racial/ethnic backgrounds who have (or had) overweight/obesity to learn about their experiences trying to lose weight. In this conversation, you are interested in collecting information about a time when they wanted to give up on trying to lose weight.

Your goal is to gather structured answers to the following questions. 

""" + questions_service.list_questions() + """

Ask each question one at a time, using empathetic and adult friendly language while maintaining a descriptive tone. Do not include '-' when you ask the question.  Ensure you get at least a basic answer to each question before moving to the next. Never answer for the human. If you are unsure what the human meant, ask again.

Once you have collected answers to all four questions, stop the conversation and write a single word "FINISHED"

Current conversation:
{history}
Human: {input}
AI:
"""




prompt_adaptation = """
You're a helpful assistant, helping patients adapt a scenario to their liking. The original scenario this student came with: 

Scenario: {scenario}.  

Their current request is {input}. 

Suggest an alternative version of the scenario. Keep the language and content as similar as possible, while fulfiling the patient's request. 

Return your answer as a JSON file with a single entry called 'new_scenario'

"""

examples = ExamplesService(repo)
examples.get_examples("./resources/examples1.json")
example_set = examples.create_key_answers()

prompt_one_shot = """

{main_prompt}

Example:
""" + examples.create_included_question_answers() + """

The scenario based on these responses: """ + examples.scenario_answer + """

Your task:
Create scenario based on the following answers:
""" + questions_service.create_question_keys() + """


{end_prompt}
Your output should be a JSON file with a single entry called 'output_scenario'

"""


## Note that we have pulled out the main part of the prompt ... so we can easily play with different options here -- see lc_scenario_prompts 


end_prompt_core = "Create a scenario based on these responses, using adult friendly language."


extraction_prompt = """
You are an expert extraction algorithm. 
Only extract relevant information from the Human answers in the text.
Use only the words and phrases that the text contains. 
If you do not know the value of an attribute asked to extract, 
return null for the attribute's value. 

You will output a JSON with """ + questions_service.list_keys() + """ keys. 

These correspond to the following questions 

""" + questions_service.list_questions() + """

Message to date: {conversation_history}

Remember, only extract text that is in the messages above and do not change it. 
"""
