from PyQt5.QtWidgets import QApplication
from classes import GameWindow
import sys


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = GameWindow()
    window.show()
    sys.exit(app.exec_())