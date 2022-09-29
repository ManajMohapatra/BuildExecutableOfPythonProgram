import os
from PySide6.QtWidgets import QWidget, QComboBox, QSizePolicy, QVBoxLayout
from PySide6.QtCore import Qt
from logDefs import warning

class ControlWidget(QWidget):
	def __init__(self, mainWindow = None, folderName = "",*args, **kwargs):
		super(ControlWidget,self).__init__(*args,**kwargs)
		if(mainWindow):
			self._mainWindow = mainWindow
		layout = QVBoxLayout()
		layout.setAlignment(Qt.AlignTop)
		self.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
		self.setLayout(layout)
		self.addImageList(folderName)
		self.makeConnection()

	def addImageList(self,folderName):
		self.imageListWidget = QComboBox(self)
		self.imageListWidget.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
		for file in os.listdir(folderName):
			if(file.endswith(".jpg") or file.endswith(".png")):
				self.imageListWidget.addItem(file.split(".")[0])
		self.layout().addWidget(self.imageListWidget)

	def makeConnection(self):
		if(self._mainWindow):
			self.imageListWidget.currentIndexChanged.connect(self._mainWindow.changeImage)
		else:
			warning("Mainwidow not found")
