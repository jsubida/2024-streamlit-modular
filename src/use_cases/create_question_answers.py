from src.entities.question_answer import QuestionAnswer


def execute(question_answers: list[QuestionAnswer]) -> str:
    """Create a string of questions and answers based on a list of question answers.
    
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
    return "\n".join([f"Question: {qa.question}\nAnswer: {qa.answer}" for qa in question_answers])
