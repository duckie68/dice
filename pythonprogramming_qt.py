#!/usr/bin/env python

import sys
from PyQt4 import QtGui, QtCore


class Window(QtGui.QMainWindow):

    def __init__(self):
        super(Window, self).__init__()
        self.setGeometry(50, 50, 800, 600)
        self.setWindowTitle('Duckie is pretty good at this')
        self.setWindowIcon(QtGui.QIcon('dice-twenty-faces-twenty.png'))

        extractAction = QtGui.QAction('&GET TO THE CHOPPAH!!', self)
        extractAction.setShortcut('Ctrl+Q')
        extractAction.setStatusTip('Leave the App')
        extractAction.triggered.connect(self.close_application)

        self.statusBar()

        mainMenu = self.menuBar()
        fileMenu = mainMenu.addMenu('&File')
        fileMenu.addAction(extractAction)

        self.home()

    def home(self):
        btn = QtGui.QPushButton("Quit", self)
        btn.clicked.connect(self.close_application)

        btn.resize(btn.sizeHint())
        #  Also x and y
        #  Or btn.minimumSizeHint()

        btn.move(100, 100)

        self.show()

    def close_application(self):
        print('This was a custom function!')
        sys.exit()





def run():
    app = QtGui.QApplication(sys.argv)
    GUI = Window()
    sys.exit(app.exec_())

run()