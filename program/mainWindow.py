import os
from PySide6.QtWidgets import (
    QMainWindow, QWidget, QHBoxLayout)

from imageWidget import ImageStackWidget
from controlWidget import ControlWidget
from logDefs import critical, error, warning, info, debug, info


class MainWindow(QMainWindow):
    def __init__(self, title="", folder = '', *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        self._folder = folder
        self.setTitle(title)
        self.addCentralWidget()
        self.addImageWidget()
        self.addControlWidget()
        self.show()

    def setTitle(self, title):
        """ title of the main window """
        if(title == ""):
            title = "Mainwindow"
        self.setWindowTitle(title)

    def addCentralWidget(self):
        """ create central widget """
        # set layout of main window
        layout = QHBoxLayout()
        self.centralWidget = QWidget()
        self.centralWidget.setLayout(layout)
        self.setCentralWidget(self.centralWidget)

    def addImageWidget(self):
        self.imageStackWidget = ImageStackWidget(self,self._folder)
        self.centralWidget.layout().addWidget(self.imageStackWidget)

    def addControlWidget(self):
        self.controlWidget = ControlWidget(mainWindow = self, folderName=self._folder)
        self.centralWidget.layout().addWidget(self.controlWidget)

    def changeImage(self, index):
        self.imageStackWidget.setIndex(index)
