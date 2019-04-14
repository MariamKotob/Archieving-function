
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QInputDialog, QLineEdit, QFileDialog
import os, subprocess, socket

#---------------------------Client module------------------------
class myclient():
    def __init__(self, data):
        self.data = data
        self.s = socket.socket()
        self.host = 'localhost'
        self.port = 8080

        self.s.connect((self.host, self.port))
        print("connected from client")


        self.s.send(data.encode())
        print("data sent suceccfully")

#---------------------------GUI window module------------------------
class Ui_Main(object):
    filename = " "
    def setupUi(self, Main):
        Main.setObjectName("Main")
        Main.setWindowModality(QtCore.Qt.ApplicationModal)
        Main.resize(373, 163)
        Main.setToolButtonStyle(QtCore.Qt.ToolButtonFollowStyle)
        self.centralwidget = QtWidgets.QWidget(Main)
        self.centralwidget.setObjectName("centralwidget")
        self.pathtxt = QtWidgets.QTextEdit(self.centralwidget)
        self.pathtxt.setEnabled(True)
        self.pathtxt.setGeometry(QtCore.QRect(93, 10, 261, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pathtxt.setFont(font)
        self.pathtxt.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.pathtxt.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.pathtxt.setObjectName("pathtxt")
        self.strtbtn = QtWidgets.QPushButton(self.centralwidget)
        self.strtbtn.setGeometry(QtCore.QRect(0, 90, 75, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.strtbtn.setFont(font)
        self.strtbtn.setObjectName("strtbtn")
        self.loadFilebtn = QtWidgets.QToolButton(self.centralwidget)
        self.loadFilebtn.setGeometry(QtCore.QRect(10, 11, 71, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.loadFilebtn.setFont(font)
        self.loadFilebtn.setAutoFillBackground(False)
        self.loadFilebtn.setIconSize(QtCore.QSize(16, 8))
        self.loadFilebtn.setShortcut("")
        self.loadFilebtn.setCheckable(False)
        self.loadFilebtn.setAutoRaise(False)
        self.loadFilebtn.setObjectName("loadFilebtn")
        self.cnclbtn = QtWidgets.QPushButton(self.centralwidget)
        self.cnclbtn.setGeometry(QtCore.QRect(270, 90, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.cnclbtn.setFont(font)
        self.cnclbtn.setObjectName("cnclbtn")
        Main.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(Main)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 373, 21))
        self.menubar.setObjectName("menubar")
        Main.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(Main)
        self.statusbar.setObjectName("statusbar")
        Main.setStatusBar(self.statusbar)

        self.retranslateUi(Main)
        QtCore.QMetaObject.connectSlotsByName(Main)

        # ---------------------------Buttons functionality------------------------
        self.loadFilebtn.clicked.connect(self.loadfile)
        self.strtbtn.clicked.connect(self.start)

    def retranslateUi(self, Main):
        _translate = QtCore.QCoreApplication.translate
        Main.setWindowTitle(_translate("Main", "ZIP Compressor"))
        self.strtbtn.setText(_translate("Main", "Go"))
        self.loadFilebtn.setText(_translate("Main", "..."))
        self.cnclbtn.setText(_translate("Main", "Cancel"))

    #Method for the browse button to load the file
    def loadfile(self):
        self.options = QFileDialog.Options()
        self.options |= QFileDialog.DontUseNativeDialog
        name, mn =  QFileDialog.getOpenFileName()
        getpath, getfile = os.path.split(name)
        self.pathtxt.setPlainText(name)
        print(name)
        print(mn)
        self.filename = str(getfile)

    #Method for the GO button to start working
    def start(self):
        print("about to start client")
        Aclient = myclient(self.filename)
        priny("created client")

#-------------------start of main--------------------------------------------
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Main = QtWidgets.QMainWindow()
    ui = Ui_Main()
    ui.setupUi(Main)
    Main.show()
    sys.exit(app.exec_())




