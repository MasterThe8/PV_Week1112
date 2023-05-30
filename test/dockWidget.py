import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QTextEdit, QDockWidget
from PyQt5.QtCore import Qt


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('DockWidget Example')
        self.initUI()

    def initUI(self):
        self.text_edit = QTextEdit()
        self.setCentralWidget(self.text_edit)

        dock_widget = QDockWidget('Dock Widget', self)
        dock_widget.setAllowedAreas(Qt.LeftDockWidgetArea | Qt.RightDockWidgetArea)
        dock_widget.setWidget(QTextEdit())
        self.addDockWidget(Qt.RightDockWidgetArea, dock_widget)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
