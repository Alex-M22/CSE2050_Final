from xmlparser import XMLParser
from question import Question
from choiceimq import ChoiceImageQuestion
from choiceq import ChoiceQuestion
from DMVDriverTestUI import DMVTestUI
from PyQt5 import QtWidgets
import sys



def main():
    quiz_parse = XMLParser("florida_drivers_test.xml").parse_questions()
    app = QtWidgets.QApplication(sys.argv)

    ui = DMVTestUI()
    ui.setupUi(ui, quiz_parse)
    ui.show()


    sys.exit(app.exec_())

main()
