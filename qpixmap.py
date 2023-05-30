import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *


def window():
    app = QApplication(sys.argv)
    win = QWidget()
    l1 = QLabel()
    # i = QImage
    # # p = QPixmap("py.png")
    # p = QPixmap
    # p.load('py.png')
    # p.fromImage(i)
    # p.copy()
    # print(p)
    l1.setPixmap(QPixmap("py.png"))
    # l1.setPixmap(p)

    vbox = QVBoxLayout()
    vbox.addWidget(l1)
    win.setLayout(vbox)
    win.setWindowTitle("QPixmap Demo")
    win.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    window()
