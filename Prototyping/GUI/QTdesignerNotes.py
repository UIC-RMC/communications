#https://www.youtube.com/watch?v=FVpho_UiDAY
#Run QTdesigner (CMD): pyqt5-tools designer
#Compile generated UI file (CMD): pyuic5 -x filename.ui -o desiredFilename.py

from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys

def window():
    app = QApplication(sys.argv)
    win = QMainWindow()
    win.setGeometry(200, 200, 640, 480)
    win.setWindowTitle('ATLAS Control Prototype')

    label = QtWidgets.QLabel(win)
    label.setText('Test Label')
    label.move(50,50)

    win.show()
    sys.exit(app.exec_())

window()