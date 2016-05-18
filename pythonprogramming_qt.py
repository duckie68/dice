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

        print(self.style().objectName())
        self.styleChoice = QtGui.QLabel('Windows', self)

        comboBox = QtGui.QComboBox(self)
        comboBox.addItem('motif')
        comboBox.addItem('Windows')
        comboBox.addItem('cde')
        comboBox.addItem('Plastique')
        comboBox.addItem('windowsVista')

        comboBox.move(50, 250)
        self.styleChoice.move(50, 150)
        comboBox.activated[str].connect(self.style_choice)

        self.home()

    def style_choice(self, text):
        self.styleChoice.setText(text)
        QtGui.QApplication.setStyle(QtGui.QStyleFactory.create(text))

    def home(self):
        btn = QtGui.QPushButton("Get the hell out of Dodge", self)
        btn.clicked.connect(self.close_application)

        btn.resize(btn.sizeHint())
        #  Also x and y
        #  Or btn.minimumSizeHint()

        btn.move(100, 100)

        extractAction = QtGui.QAction(QtGui.QIcon('helicopter-icon.png'), 'Flee the scene', self)
        extractAction.triggered.connect(self.close_application)

        self.toolbar = self.addToolBar('Extraction')
        self.toolbar.addAction(extractAction)

        fontChoice = QtGui.QAction('Pick a font!', self)
        fontChoice.triggered.connect(self.font_choice)

        # self.toolbar = self.addToolBar('Font')
        # Uncommenting above makes a new toolbar
        self.toolbar.addAction(fontChoice)

        color = QtGui.QColor(0, 0, 0)

        fontColor = QtGui.QAction('Font bg color', self)
        fontColor.triggered.connect(self.color_picker)
        self.toolbar.addAction(fontColor)

        checkBox = QtGui.QCheckBox('Embiggen Window', self)
        # Need to find out why not all text showing
        checkBox.move(200, 200)
        #  checkBox.toggle() would default with a checkmark
        checkBox.stateChanged.connect(self.enlarge_window)

        self.progress = QtGui.QProgressBar(self)
        self.progress.setGeometry(50, 70, 400, 20)

        self.btn = QtGui.QPushButton('Fake Download', self)
        self.btn.move(200, 120)
        self.btn.clicked.connect(self.fake_download)

        cal = QtGui.QCalendarWidget(self)
        cal.move(500, 200)
        cal.resize(200, 200)

        self.show()

    def color_picker(self):
        color = QtGui.QColorDialog.getColor()
        self.styleChoice.setStyleSheet('QWidget { background-color: %s}' % color.name())

    def font_choice(self):
        font, valid = QtGui.QFontDialog.getFont()
        if valid:
            self.styleChoice.setFont(font)

    def fake_download(self):
        self.completed = 0

        while self.completed < 100:
            self.completed += 0.0001
            self.progress.setValue(self.completed)

    def enlarge_window(self, state):
        if state == QtCore.Qt.Checked:
            self.setGeometry(50, 50, 1000, 800)
        else:
            self.setGeometry(50, 50, 800, 600)

    def close_application(self):
        print('This was a custom function!')

        choice = QtGui.QMessageBox.question(self, 'Extract', 'Get into the choppah?',
                                            QtGui.QMessageBox.Yes | QtGui.QMessageBox.No)
        if choice == QtGui.QMessageBox.Yes:
            print('Extracting Noooooow!')
            sys.exit()

        sys.exit()





def run():
    app = QtGui.QApplication(sys.argv)
    GUI = Window()
    sys.exit(app.exec_())

run()