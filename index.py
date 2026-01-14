import sys
from Vue.Initializer.main import Final
from PySide6.QtWidgets import QApplication,QMainWindow
if __name__ == "__main__":
    app = QApplication([])
    window = QMainWindow()
    ui = Final(window)
    window.show()
    sys.exit(app.exec())