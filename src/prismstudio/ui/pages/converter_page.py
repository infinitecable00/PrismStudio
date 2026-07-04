from pathlib import Path

from PySide6.QtCore import Qt
from PySide6.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QLabel,
    QListWidget,
    QPushButton,
    QFileDialog,
    QComboBox,
    QHBoxLayout,
    QMessageBox,
)

from src.prismstudio.core.converter import Converter


class ConverterPage(QWidget):

    def __init__(self):
        super().__init__()

        self.converter = Converter()

        self.output_folder = ""

        layout = QVBoxLayout(self)

        title = QLabel("🎵 Prism Studio Converter")
        title.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.file_list = QListWidget()

        self.format_box = QComboBox()
        self.format_box.addItems([
            "wav",
            "flac",
            "mp3",
            "ogg",
            "aac"
        ])

        choose = QPushButton("Choose Output Folder")
        choose.clicked.connect(self.choose_folder)

        convert = QPushButton("Convert")
        convert.clicked.connect(self.convert_files)

        buttons = QHBoxLayout()

        buttons.addWidget(self.format_box)
        buttons.addWidget(choose)
        buttons.addWidget(convert)

        layout.addWidget(title)
        layout.addWidget(self.file_list)
        layout.addLayout(buttons)

        self.setAcceptDrops(True)

    def choose_folder(self):

        folder = QFileDialog.getExistingDirectory(
            self,
            "Choose Output Folder"
        )

        if folder:
            self.output_folder = folder

    def dragEnterEvent(self,event):

        if event.mimeData().hasUrls():
            event.acceptProposedAction()

    def dropEvent(self,event):

        for url in event.mimeData().urls():

            self.file_list.addItem(url.toLocalFile())

    def convert_files(self):

        if not self.output_folder:

            QMessageBox.warning(
                self,
                "Output Folder",
                "Please choose an output folder first."
            )

            return

        extension = self.format_box.currentText()

        success = 0

        for i in range(self.file_list.count()):

            filename = self.file_list.item(i).text()

            if self.converter.convert_file(
                filename,
                self.output_folder,
                extension,
            ):
                success += 1

        QMessageBox.information(
            self,
            "Finished",
            f"Converted {success} file(s)."
        )
