class Question:
    def __init__(self):
        self._question_text = ""
        self._answer = ""

    def set_text(self, t):
        self._question_text = t

    def set_answer(self, at):
        self._answer = at

    def check_answer(self, ans_t):
        if ans_t == self._answer:
            return True
        return False
