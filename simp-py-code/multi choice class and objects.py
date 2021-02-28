

class Question:
    def __init__(self, prompt, answer):
        self.prompt = prompt
        self.answer = answer

question_prompt = ["what is my name? \n" , "When was I born? \n", "Name my by color \n"]

questions = [Question(question_prompt[0], "Michael"),
             Question(question_prompt[1], 2002),
             Question(question_prompt[2], "blue")]

def score(questions):
    score = 0
    for question in questions:
        answer = input(question.prompt)
        if answer == question.answer:
            score += 1
    print("You got " + str(score) + "/" + str(len(questions))) 
score(questions)