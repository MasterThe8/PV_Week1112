from PyQt5.QtWidgets import QListWidget, QListWidgetItem, QApplication, QMainWindow, QLabel, QVBoxLayout, QWidget
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtCore import Qt, QMimeData


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.list_widget = QListWidget()

        self.pixmap_label = QLabel()
        self.pixmap_label.setAlignment(Qt.AlignCenter)
        self.pixmap_label.setAcceptDrops(True)

        vbox = QVBoxLayout()
        vbox.addWidget(self.list_widget)
        vbox.addWidget(self.pixmap_label)

        container = QWidget()
        container.setLayout(vbox)
        self.setCentralWidget(container)
        self.setWindowTitle("Drag and Drop Example")

        self.list_widget.setAcceptDrops(True)

    def dragEnterEvent(self, event):
        if event.mimeData().hasUrls() or event.mimeData().hasText():
            event.acceptProposedAction()

    def dragMoveEvent(self, event):
        event.acceptProposedAction()

    def dropEvent(self, event):
        if event.mimeData().hasUrls():
            for url in event.mimeData().urls():
                image_path = url.toLocalFile()
                self.addImageToList(image_path)

            event.acceptProposedAction()

        elif event.mimeData().hasText():
            image_path = event.mimeData().text()
            self.addImageToList(image_path)
            event.acceptProposedAction()

    def addImageToList(self, image_path):
        pixmap = QPixmap(image_path)

        # Tambahkan pixmap ke QLabel
        current_pixmap = self.pixmap_label.pixmap()
        if current_pixmap is not None:
            pixmap = pixmap.scaled(current_pixmap.size(), Qt.KeepAspectRatio)  # Ukuran pixmap ditetapkan sama dengan pixmap saat ini

        self.pixmap_label.setPixmap(pixmap)

        # Tambahkan nama file gambar ke QListWidget
        item = QListWidgetItem(image_path)
        self.list_widget.addItem(item)


if __name__ == "__main__":
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec_()
