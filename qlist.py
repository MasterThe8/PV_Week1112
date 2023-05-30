from PyQt5.QtWidgets import *

import sys


class myListWidget(QListWidget):

    def Clicked(self, item):
        QMessageBox.warning(self, "ListWidget", "You clicked: " + item.text())

    def Moved(self, item):
        print(item.text())


def main():
    app = QApplication(sys.argv)
    listWidget = myListWidget()

    # Resize width and height
    listWidget.resize(300, 120)

    listWidget.addItem("Item 1")
    listWidget.addItem("Item 2")
    listWidget.addItem("Item 3")
    listWidget.addItem("Item 4")

    listWidget.setWindowTitle('PyQT QListwidget Demo')
    listWidget.itemClicked.connect(listWidget.Clicked)
    listWidget.currentItemChanged.connect(listWidget.Moved)

    listWidget.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
