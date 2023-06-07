import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Text Editor')
        self.canvas = QLabel(self)
        self.canvas.setGeometry(10, 10, 800, 600)
        self.canvas.setPixmap(QPixmap(400, 300))
        self.canvas.setAlignment(Qt.AlignCenter)
        self.canvas.mousePressEvent = self.canvas_mousePressEvent
        
        self.font_list = QListWidget(self)
        self.font_list.setGeometry(420, 10, 150, 300)
        self.font_list.currentTextChanged.connect(self.set_text_font)
        
        self.bg_color_btn = QPushButton('Canvas Color', self)
        self.bg_color_btn.setGeometry(420, 360, 150, 30)
        self.bg_color_btn.clicked.connect(self.set_canvas_color)

    def set_text_font(self, font):
        current_font = self.font_list.currentItem().text()
        text = self.canvas.text()
        self.canvas.setFont(QFont(current_font))
        self.canvas.setText(text)
        self.canvas.adjustSize()
    
    def canvas_mousePressEvent(self, event):
        if event.button() == Qt.RightButton:
            dialog = TextDialog(self)
            if dialog.exec_() == QDialog.Accepted:
                text = dialog.get_text()
                x = event.x()
                y = event.y()
                pixmap = self.canvas.pixmap()
                painter = QPainter(pixmap)
                font = self.canvas.font()
                font_metrics = QFontMetrics(font)
                text_width = font_metrics.width(text)
                text_height = font_metrics.height()
                center_x = x - text_width // 2
                center_y = y + text_height // 2
                painter.setFont(font)
                painter.setPen(QColor(Qt.red))
                painter.drawText(center_x, center_y, text)
                painter.end()
                self.canvas.setPixmap(pixmap)

    def set_canvas_color(self):
        color = QColorDialog.getColor()
        if color.isValid():
            pixmap = self.canvas.pixmap()
            pixmap.fill(color)
            self.canvas.setPixmap(pixmap)

class TextDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle('Add Text')
        
        layout = QVBoxLayout()
        
        self.text_input = QLineEdit()
        layout.addWidget(self.text_input)
        
        self.button_ok = QPushButton('OK')
        self.button_ok.clicked.connect(self.accept)
        layout.addWidget(self.button_ok)
        
        self.setLayout(layout)

    def get_text(self):
        return self.text_input.text()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    
    window.font_list.addItems(QFontDatabase().families())
    window.show()
    
    sys.exit(app.exec_())
