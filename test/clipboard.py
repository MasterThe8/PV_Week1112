import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QAction, QLabel, QVBoxLayout, QWidget, QPushButton, QGridLayout, QTextEdit, QMessageBox
from PyQt5.QtGui import QPainter, QPen, QColor, QClipboard
from PyQt5.QtCore import Qt


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Clipboard Example')
        self.clipboard = QApplication.clipboard()
        self.initUI()

    def initUI(self):
        central_widget = QWidget()
        layout = QGridLayout()
        central_widget.setLayout(layout)

        self.text_edit = QTextEdit()
        layout.addWidget(self.text_edit, 0, 0, 1, 2)

        copy_button = QPushButton('Copy')
        copy_button.clicked.connect(self.copy_text)
        layout.addWidget(copy_button, 1, 0)

        paste_button = QPushButton('Paste')
        paste_button.clicked.connect(self.paste_text)
        layout.addWidget(paste_button, 1, 1)

        self.setCentralWidget(central_widget)

    def copy_text(self):
        text = self.text_edit.toPlainText()
        if text:
            self.clipboard.setText(text)
            QMessageBox.information(self, 'Copied', 'Text copied to clipboard.')

    def paste_text(self):
        text = self.clipboard.text()
        if text:
            self.text_edit.setPlainText(text)
            QMessageBox.information(self, 'Pasted', 'Text pasted from clipboard.')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
