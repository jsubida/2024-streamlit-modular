from src.entities.question_answer import QuestionAnswer


def execute(questions: list[QuestionAnswer]) -> str:
    """List the questions in a formatted string.
    
    Example:
        - What happened to make you want to give up?
        - How did you feel emotionally at the time? 
        - What was the worst part of this experience?
        - How did the whole situation end? (did you give up? did you keep on going?)
        - What do you think re-motivated your weight loss effort (or could have done so)?
    """
    return "\n".join([f"- {q.question}" for q in questions])
