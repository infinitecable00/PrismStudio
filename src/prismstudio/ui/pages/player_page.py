from PySide6.QtCore import Qt
from PySide6.QtWidgets import QLabel, QVBoxLayout, QWidget


class PlayerPage(QWidget):
    def __init__(self):
        super().__init__()

        layout = QVBoxLayout(self)

        title = QLabel("▶ Audio Player")
        title.setAlignment(Qt.AlignmentFlag.AlignCenter)

        layout.addWidget(title)
