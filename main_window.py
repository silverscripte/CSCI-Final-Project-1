from PyQt5 import QtCore, QtGui, QtWidgets
from voting_window import Ui_vote_window
from results_window import Ui_result_window

class Ui_mainwindow(object):
    ##function to open voting menu
    def voting_open(self):
        self.window_vote = QtWidgets.QWidget()
        self.ui_vote = Ui_vote_window()
        self.ui_vote.setupUi(self.window_vote)
        self.window_vote.show()

    ##opens result window
    def open_results(self):
        self.window_results = QtWidgets.QWidget()
        self.ui_results = Ui_result_window()
        self.ui_results.setupUi(self.window_results)
        self.window_results.show()


    def exit(self):
        mainwindow.close()
        self.open_results()

    def setupUi(self, mainwindow):
        mainwindow.setObjectName("mainwindow")
        mainwindow.resize(281, 112)
        mainwindow.setMaximumSize(QtCore.QSize(286, 300))
        self.Vote_Menu = QtWidgets.QLabel(mainwindow)
        self.Vote_Menu.setGeometry(QtCore.QRect(110, 20, 61, 16))
        self.Vote_Menu.setObjectName("Vote_Menu")

        ##setting vote button to open voting menu
        self.vote_button = QtWidgets.QPushButton(mainwindow, clicked = lambda: self.voting_open())

        self.vote_button.setGeometry(QtCore.QRect(10, 70, 93, 28))
        self.vote_button.setObjectName("vote_button")
        self.buttonGroup = QtWidgets.QButtonGroup(mainwindow)
        self.buttonGroup.setObjectName("buttonGroup")
        self.buttonGroup.addButton(self.vote_button)
        self.exit_button = QtWidgets.QPushButton(mainwindow, clicked=lambda: self.exit())
        self.buttonGroup.addButton(self.exit_button)
        self.exit_button.setGeometry(QtCore.QRect(170, 70, 93, 28))
        self.exit_button.setObjectName("exit_button")

        self.retranslateUi(mainwindow)
        QtCore.QMetaObject.connectSlotsByName(mainwindow)




    def retranslateUi(self, mainwindow):
        _translate = QtCore.QCoreApplication.translate
        mainwindow.setWindowTitle(_translate("mainwindow", "Vote Menu"))
        self.Vote_Menu.setText(_translate("mainwindow", "Vote Menu"))
        self.vote_button.setText(_translate("mainwindow", "Vote"))
        self.exit_button.setText(_translate("mainwindow", "Exit"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    mainwindow = QtWidgets.QDialog()
    ui = Ui_mainwindow()
    ui.setupUi(mainwindow)
    mainwindow.show()
    sys.exit(app.exec_())
