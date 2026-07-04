import sys

from PySide6.QtWidgets import QApplication

from src.prismstudio.main_window import MainWindow
from src.prismstudio.themes.theme_manager import stylesheet


def run():
    app = QApplication(sys.argv)

    app.setApplicationName("Prism Studio")
    app.setOrganizationName("InfiniteCable Software")

    app.setStyleSheet(stylesheet())

    window = MainWindow()
    window.show()

    sys.exit(app.exec())
