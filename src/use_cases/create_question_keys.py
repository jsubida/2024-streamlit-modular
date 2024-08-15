from src.entities.question_answer import QuestionAnswer


def execute(question_answers: list[QuestionAnswer]) -> str:
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
    return "\n".join([f"Question: {qa.question}\nAnswer: {{{qa.key}}}" for qa in question_answers])
