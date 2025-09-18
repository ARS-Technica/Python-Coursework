class Question:
    def __init__(self, question_text, answer_text):
        self.question_text = question_text
        self.answer_text = answer_text

new_question = Question("Something here", "False")
print(new_question.question_text)
