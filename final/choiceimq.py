from question import Question
from choiceq import ChoiceQuestion

class ChoiceImageQuestion(ChoiceQuestion):
    def __init__(self):
        self._img_bytes = None
        super().__init__()


    def set_image(self, img):
        self._img_bytes = open(img, "rb").read()

    def display(self, layout):
        pass