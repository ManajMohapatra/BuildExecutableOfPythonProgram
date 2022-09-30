import sys, os
from PySide6.QtWidgets import QApplication
from mainWindow import MainWindow

if __name__ == "__main__":
	CURRENT_DIR = "."
	if hasattr(sys, '_MEIPASS'):
		CURRENT_DIR = sys._MEIPASS
	app = QApplication(sys.argv)
	folder = input("Please enter path to images folder or just press ENTER to select default path")
	if(not folder or not os.path.isdir(folder)):
		folder = CURRENT_DIR + os.sep + "images"
	folder += os.sep
	print("Images will taken from folder: {}".format(folder))
	cameraMainWindow = MainWindow(title = "Nature", folder = folder)
	sys.exit(app.exec())