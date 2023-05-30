import sys
from PyQt5.QtWidgets import QApplication, QDialog, QVBoxLayout, QLabel, QPushButton, QStatusBar


class MyDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Status Bar Example')
        self.initUI()

    def initUI(self):
        layout = QVBoxLayout()

        self.status_bar = QStatusBar()
        self.status_bar.showMessage('Ready')
        layout.addWidget(self.status_bar)

        label = QLabel('Click the button to update the status:')
        layout.addWidget(label)

        button = QPushButton('Update Status')
        button.clicked.connect(self.update_status)
        layout.addWidget(button)

        self.setLayout(layout)

    def update_status(self):
        self.status_bar.showMessage('Status updated')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    dialog = MyDialog()
    dialog.show()
    sys.exit(app.exec_())
