class Question:
    def __init__(self, prompt, answer_up, answer_low):
        self.prompt = prompt
        self.answer_up = answer_up
        self.answer_low = answer_low


class QuestionL:
    def __init__(self, prompt, lis):
        self.prompt = prompt
        self.lis = lis
