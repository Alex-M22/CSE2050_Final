# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'DMVDriverTestUI.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from quiz_list import Quiz_list
from choiceimq import ChoiceImageQuestion


class DMVTestUI(QtWidgets.QMainWindow):
    def setupUi(self, MainWindow, ql):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1000, 900)
        self.setFixedHeight(900)
        self.setFixedWidth(1000)
        self._central_widget = QtWidgets.QWidget(MainWindow)
        self._central_widget.setObjectName("_central_widget")
        self.gridLayout = QtWidgets.QGridLayout(self._central_widget)
        self.gridLayout.setObjectName("gridLayout")
        self._quit = QtWidgets.QPushButton(self._central_widget)
        self._quit.setObjectName("_quit")
        self.gridLayout.addWidget(self._quit, 4, 2, 1, 1)
        self._photo = QtWidgets.QLabel(self._central_widget)
        self._photo.setObjectName("_photo")
        self.gridLayout.addWidget(self._photo, 0, 0, 1, 3)
        self._question = QtWidgets.QLabel(self._central_widget)
        self._question.setObjectName("_question")
        self.gridLayout.addWidget(self._question, 1, 0, 1, 3)

        self._comments = QtWidgets.QLabel(self._central_widget)
        self._comments.setObjectName("_comments")
        self.gridLayout.addWidget(self._comments, 3, 0, 1, 3)

        self._num_correct = QtWidgets.QLabel(self._central_widget)
        self._num_correct.setObjectName("_num_correct")
        self.gridLayout.addWidget(self._num_correct, 4, 0, 1, 1)
        self._next = QtWidgets.QPushButton(self._central_widget)
        self._next.setObjectName("_next")
        self.gridLayout.addWidget(self._next, 4, 1, 1, 1)
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setSizeConstraint(QtWidgets.QLayout.SetFixedSize)
        self.formLayout.setRowWrapPolicy(QtWidgets.QFormLayout.WrapAllRows)
        self.formLayout.setObjectName("formLayout")
        self._answer1 = QtWidgets.QRadioButton(self._central_widget)
        self._answer1.setObjectName("_answer1")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self._answer1)
        self._answer2 = QtWidgets.QRadioButton(self._central_widget)
        self._answer2.setObjectName("_answer2")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self._answer2)
        self._answer3 = QtWidgets.QRadioButton(self._central_widget)
        self._answer3.setObjectName("_answer3")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self._answer3)
        self._answer4 = QtWidgets.QRadioButton(self._central_widget)
        self._answer4.setObjectName("_answer4")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self._answer4)
        self.gridLayout.addLayout(self.formLayout, 2, 0, 1, 3)
        MainWindow.setCentralWidget(self._central_widget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 460, 18))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self._quiz_list = Quiz_list(ql)
        self._cur_question = next(self._quiz_list)
        self._correct = 0
        self._enabled = False

        self._num_correct.setText(f"{'Question'} {self._quiz_list.index() + 1} {'of'} {self._quiz_list.size()}{'   | Correct: '}{self._correct}{' / '}{self._quiz_list.size()}")
        self.set_ui()

        self._answer1.clicked.connect(self.checking_1)
        self._answer2.clicked.connect(self.checking_2)
        self._answer3.clicked.connect(self.checking_3)
        self._answer4.clicked.connect(self.checking_4)

        # self._num_correct.setText(_translate("MainWindow", "Question num1 of num2   | Correct: num3 / num2 "))
        self._next.clicked.connect(self.go_next)
        self._quit.clicked.connect(self.close)


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "DMV Driver Test"))
        self._quit.setText(_translate("MainWindow", "Quit Quiz"))
        # self._photo.setText(_translate("MainWindow", "Picture"))
        # self._question.setText(_translate("MainWindow", "Question"))
        self._next.setText(_translate("MainWindow", "Next Question"))
        # self._answer1.setText(_translate("MainWindow", "ans1"))
        # self._answer2.setText(_translate("MainWindow", "ans2"))
        # self._answer3.setText(_translate("MainWindow", "ans3"))
        # self._answer4.setText(_translate("MainWindow", "ans4"))
        self._question.setStyleSheet("font-size:20px;font-weight:600")
        self._answer1.setStyleSheet("font-size:18px;font-weight:400")
        self._answer2.setStyleSheet("font-size:18px;font-weight:400")
        self._answer3.setStyleSheet("font-size:18px;font-weight:400")
        self._answer4.setStyleSheet("font-size:18px;font-weight:400")
        self._comments.setStyleSheet("font-size:16px;font-weight:400")
        self._num_correct.setStyleSheet("font-size:16px;font-weight:400")
        self._comments.setWordWrap(True)
        self._question.setWordWrap(True)

    def set_ui(self):
        self._comments.setVisible(False)

        self._answer1.setText(self._cur_question._choices[0].strip())
        self._answer2.setText(self._cur_question._choices[1].strip())
        self._answer3.setText(self._cur_question._choices[2].strip())
        self._answer4.setText(self._cur_question._choices[3].strip())
        self._question.setText(self._cur_question._question_text.strip())
        if isinstance(self._cur_question, ChoiceImageQuestion):
            self.load_image()
            self._pic_label.setVisible(True)
            self._photo.setVisible(True)

        else:
            self._pic_label.setVisible(False)
            self._photo.setVisible(False)
            

    def load_image(self):
        my_image = QtGui.QImage()
        my_image.loadFromData(self._cur_question._img_bytes) # loadFromData also accepts images as a byte-array/string of bytes
        self._pic_label = QtWidgets.QLabel(self._photo) # choose a parent, such as a layout, or existing label where you want to show your image
        w = 1000
        h = 200
        pixmap = QtGui.QPixmap.fromImage(my_image)
        # Scale the image to fit your label
        # It's a good idea to keep the aspect ratio so your image does not get distorted
        scaled_img = pixmap.scaled(w, h, QtCore.Qt.KeepAspectRatio) # or Qt.IgnoreAspectRatio
        self._pic_label.setPixmap(pixmap)

    def go_next(self):
        if not self._enabled:
            pass
        else:
            self._cur_question = next(self._quiz_list)
            if self._cur_question is None:
                self.end_screen()
            else:
                self._num_correct.setText(f"{'Question'} {self._quiz_list.index() + 1} {'of'} {self._quiz_list.size()}{'   | Correct: '}{self._correct}{' / '}{self._quiz_list.size()}")
                self.set_ui()
                self.reset_buttons()
                self.button_enabler()

    def checking_1(self):
        self.button_enabler()
        if self._cur_question.check_answer(self._answer1.text()):
            self._correct += 1
        

    def checking_2(self):
        self.button_enabler()
        if self._cur_question.check_answer(self._answer2.text()):
            self._correct += 1
    
    def checking_3(self):
        self.button_enabler()
        if self._cur_question.check_answer(self._answer3.text()):
            self._correct += 1

    def checking_4(self):
        self.button_enabler()
        if self._cur_question.check_answer(self._answer4.text()):
            self._correct += 1

    def button_enabler(self):
        self._enabled = not self._enabled 
        self._answer1.setDisabled(self._enabled)
        self._answer2.setDisabled(self._enabled)
        self._answer3.setDisabled(self._enabled)
        self._answer4.setDisabled(self._enabled)
        self._comments.setVisible(self._enabled)
        self._comments.setText(self._cur_question._answer_comments.strip())

    def reset_buttons(self):
        self._answer1.setCheckable(False)
        self._answer2.setCheckable(False)
        self._answer3.setCheckable(False)
        self._answer4.setCheckable(False)
        self._answer1.setCheckable(True)
        self._answer2.setCheckable(True)
        self._answer3.setCheckable(True)
        self._answer4.setCheckable(True)

    def end_screen(self):
        self._answer1.setVisible(False)
        self._answer2.setVisible(False)
        self._answer3.setVisible(False)
        self._answer4.setVisible(False)
        self._next.setVisible(False)
        self._photo.setVisible(False)
        self._pic_label.setVisible(False)
        self._comments.setVisible(False)
        self._num_correct.setVisible(False)
        self._question.setText(f'{"Your Score is "}{self._correct}{" out of "}{self._quiz_list.size()}')