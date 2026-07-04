from PySide6.QtWidgets import (
    QHBoxLayout,
    QLabel,
    QMainWindow,
    QStackedWidget,
    QStatusBar,
    QToolBar,
    QVBoxLayout,
    QWidget,
)

from src.prismstudio.ui.sidebar import Sidebar
from src.prismstudio.ui.pages.converter_page import ConverterPage
from src.prismstudio.ui.pages.player_page import PlayerPage
from src.prismstudio.ui.pages.metadata_page import MetadataPage
from src.prismstudio.ui.pages.settings_page import SettingsPage
from src.prismstudio.version import APP_NAME, VERSION


class PlaceholderPage(QWidget):

    def __init__(self, text):
        super().__init__()

        layout = QVBoxLayout(self)

        label = QLabel(text)

        label.setStyleSheet("font-size:28px;")

        layout.addStretch()
        layout.addWidget(label)
        layout.addStretch()


class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()

        self.setWindowTitle(f"{APP_NAME} {VERSION}")

        self.resize(1450,850)

        toolbar = QToolBar("Main")

        self.addToolBar(toolbar)

        self.sidebar = Sidebar()

        self.pages = QStackedWidget()

        self.pages.addWidget(ConverterPage())
        self.pages.addWidget(PlayerPage())
        self.pages.addWidget(MetadataPage())
        self.pages.addWidget(PlaceholderPage("Waveform Viewer"))
        self.pages.addWidget(PlaceholderPage("Spectrogram"))
        self.pages.addWidget(SettingsPage())

        self.sidebar.currentRowChanged.connect(
            self.pages.setCurrentIndex
        )

        root = QWidget()

        layout = QHBoxLayout(root)

        layout.addWidget(self.sidebar)

        layout.addWidget(self.pages,1)

        self.setCentralWidget(root)

        status = QStatusBar()

        status.showMessage("Ready")

        self.setStatusBar(status)
