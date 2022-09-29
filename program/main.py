import sys
from PySide6.QtWidgets import QApplication
from mainWindow import MainWindow

if __name__ == "__main__":
	app = QApplication(sys.argv)
	folder = input("Please enter path to images folder or just press ENTER to select default path")
	if(not folder):
		folder = r"./images/"
	cameraMainWindow = MainWindow(title = "Nature", folder = folder)
	sys.exit(app.exec())