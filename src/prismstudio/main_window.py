from PySide6.QtWidgets import QLabel, QMainWindow
from PySide6.QtCore import Qt


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Prism Studio")
        self.resize(1280, 720)

        label = QLabel("Welcome to Prism Studio!")

        label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.setCentralWidget(label)
