from PySide6.QtWidgets import QListWidget


class Sidebar(QListWidget):

    def __init__(self):
        super().__init__()

        self.addItems([
            "Converter",
            "Player",
            "Metadata",
            "Waveform",
            "Spectrogram",
            "Settings"
        ])

        self.setCurrentRow(0)
        self.setMaximumWidth(230)
