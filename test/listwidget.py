import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QListWidget, QListWidgetItem


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('List Widget Example')
        self.initUI()

    def initUI(self):
        list_widget = QListWidget()
        list_widget.addItem("Item 1")
        list_widget.addItem("Item 2")
        list_widget.addItem("Item 3")
        list_widget.addItem("Item 4")

        list_widget.itemClicked.connect(self.on_item_clicked)

        self.setCentralWidget(list_widget)

    def on_item_clicked(self, item):
        print(item.text())


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
