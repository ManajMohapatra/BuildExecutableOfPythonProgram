import os
from PySide6.QtWidgets import QStackedWidget, QWidget, QLabel, QSizePolicy
from PySide6.QtGui import QPixmap
from PySide6.QtCore import Qt
from logDefs import critical, error, warning, info, debug, info


class ImageStackWidget(QStackedWidget):
	def __init__(self, parent, folderName, *args, **kwargs):
		super(ImageStackWidget,self).__init__(parent, *args, **kwargs)
		self.addImages(folderName)

	def addImages(self, folderName):
		for file in os.listdir(folderName):
			if(file.endswith(".jpg") or file.endswith(".png")):
				widget = QWidget(self)
				widget.setSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
				label = QLabel(widget)
				pixmap = QPixmap(folderName + file)
				label.setPixmap(pixmap)
				self.addWidget(widget)

	def setIndex(self, index):
		if(index < self.count() and index >= 0):
			self.setCurrentIndex(index)
		else:
			warning("Index ({}) received is invalid".format(index))
