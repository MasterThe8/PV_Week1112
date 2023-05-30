import sys
from PyQt5.QtWidgets import QApplication, QLabel, QVBoxLayout, QWidget
from PyQt5.QtGui import QPixmap


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Pixmap Example')
        self.initUI()

    def initUI(self):
        layout = QVBoxLayout()

        pixmap = QPixmap('test/img.png')  # Provide the path to your image file
        if not pixmap.isNull():
            label = QLabel()
            label.setPixmap(pixmap)
            layout.addWidget(label)

        self.setLayout(layout)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
