import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QAction, QLabel, QVBoxLayout, QWidget
from PyQt5.QtGui import QPixmap, QPainter, QPen, QColor, QCursor
from PyQt5.QtCore import Qt, QPoint


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Simple Paint')
        self.drawing = False
        self.last_point = QPoint()
        self.initUI()

    def initUI(self):
        self.canvas = QLabel()
        self.canvas.setAlignment(Qt.AlignTop)
        self.canvas.setFixedSize(800, 600)
        self.canvas.setPixmap(QPixmap(800, 600))

        self.setCentralWidget(self.canvas)

        self.create_actions()
        self.create_menus()

    def create_actions(self):
        self.clear_action = QAction('Clear', self)
        self.clear_action.triggered.connect(self.clear_canvas)

    def create_menus(self):
        menubar = self.menuBar()
        file_menu = menubar.addMenu('File')
        file_menu.addAction(self.clear_action)

    def clear_canvas(self):
        self.canvas.setPixmap(QPixmap(800, 600))

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.drawing = True
            self.last_point = event.pos()
            self.setCursor(QCursor(Qt.CrossCursor))  # Change cursor to crosshair

    def mouseMoveEvent(self, event):
        if self.drawing and event.buttons() == Qt.LeftButton:
            painter = QPainter(self.canvas.pixmap())
            pen = QPen(Qt.red, 2, Qt.SolidLine)
            painter.setPen(pen)
            painter.drawLine(self.last_point, event.pos())
            painter.end()
            self.last_point = event.pos()
            self.canvas.update()

    def mouseReleaseEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.drawing = False
            self.setCursor(Qt.ArrowCursor)  # Change cursor back to default


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
