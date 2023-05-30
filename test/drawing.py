import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *


class Example(QWidget):

    def __init__(self):
        super(Example, self).__init__()
        self.initUI()

    def initUI(self):
        self.text = "hello world"
        self.setGeometry(100, 100, 400, 300)
        self.setWindowTitle('Draw Demo')
        self.show()

    def paintEvent(self, event):
        qp = QPainter()
        qp.begin(self)

        qp.setPen(QColor(Qt.cyan))

        qp.setFont(QFont('Arial', 20))
        qp.drawText(10, 30, "hello Python")

        qp.setPen(QColor(Qt.blue))
        # 10, 50 starting point
        # 100 length
        # 50 destination point
        qp.drawLine(10, 50, 100, 150)

        qp.drawRect(10, 100, 100, 50)

        qp.setPen(QColor(Qt.darkYellow))
        qp.drawEllipse(150, 50, 50, 100)

        qp.drawPixmap(220, 10, QPixmap("python.jpeg"))

        qp.fillRect(10, 175, 150, 150, QBrush(Qt.VerPattern))
        qp.fillRect(200, 175, 150, 100, QColor(Qt.blue))

        qp.end()


def main():
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
