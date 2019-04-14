
from PyQt5 import QtCore, QtGui, QtWidgets
import socket
import zipfile
import os

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(459, 188)
        self.prgrsBar = QtWidgets.QProgressBar(Form)
        self.prgrsBar.setGeometry(QtCore.QRect(0, 60, 461, 31))
        self.prgrsBar.setProperty("value", 24)
        self.prgrsBar.setObjectName("prgrsBar")
        self.cancel = QtWidgets.QPushButton(Form)
        self.cancel.setGeometry(QtCore.QRect(360, 140, 91, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.cancel.setFont(font)
        self.cancel.setObjectName("cancel")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)
        self.progressing()

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Compressing..."))
        self.cancel.setText(_translate("Form", "Cancel"))

    def progressing(self):
        self.completed = 0
        while self.completed <= 100:
            self.completed += 20
            self.prgrsBar.setValue(self.completed)

#-----------------------------server module----------------------------------------
class myserver():
    def __init__(self):
        host = 'Localhost'
        port = 8080
        address = (host, port)
        buf_size=1024
        myServer = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        myServer.bind(address)
        myServer.listen(1)
        conn, addr = myServer.accept()
        print ("Connection from: " + str(addr))

        while True:
            recdata = conn.recv(buf_size)
            recdata = recdata.decode()
            print( recdata)
            print("Data recieved")
            if recdata:
                self.ZipMyFile(recdata)
                break
        conn.close()
    ##end of the server

    ##Create the ZIPped file passing the current data to it and finally
       ## write it to the HDD
    def ZipMyFile(self, data):
        print("Before compressing")
        path, file = os.path.split(data)
        zfile = file.upper() + ".zip"
        zipfile.ZipFile(zfile, mode='w').write(file)
        print("from the loop done")
        print("Done compressing")


if __name__ == "__main__":
    import sys
    print("about to start server")
    srv = myserver()
    print("server started")
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())