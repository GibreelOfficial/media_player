import sys
from PyQt5.QtWidgets import QApplication
from ui import MediaPlayerWindow

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MediaPlayerWindow()
    window.show()
    sys.exit(app.exec_())
