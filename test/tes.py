import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

class PixMapT(QLabel):
    def __init__(self):
        super().__init__()
        self.drawing = False
        self.last_point = QPoint()
        self.font = None
        self.initUI()

    def initUI(self):
        self.canvas = QLabel(self)
        self.canvas.setAlignment(Qt.AlignTop)
        self.canvas.setGeometry(0, 0, 800, 600)
        self.canvas.setPixmap(QPixmap(800, 600))
        self.canvas.mousePressEvent = self.canvas_mousePressEvent
        
    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            if self.canvas.underMouse():
                self.drawing = True
                self.last_point = event.pos()
                self.setCursor(QCursor(Qt.CrossCursor))

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
            self.setCursor(Qt.ArrowCursor)

    def dragEnterEvent(self, event):
        if event.mimeData().hasUrls() or event.mimeData().hasText():
            event.acceptProposedAction()

    def dragMoveEvent(self, event):
        event.acceptProposedAction()

    def dropEvent(self, event):
        if event.mimeData().hasUrls():
            url = event.mimeData().urls()[0]
            pixmap = QPixmap(url.toLocalFile())
            if not pixmap.isNull():
                self.canvas.setPixmap(pixmap.scaled(self.canvas.size(), Qt.AspectRatioMode.KeepAspectRatio, Qt.TransformationMode.SmoothTransformation))
            event.acceptProposedAction()
            
    def canvas_mousePressEvent(self, event):
        if event.button() == Qt.RightButton:
            clipboard = QApplication.clipboard()
            text = clipboard.text()
            x = event.x()
            y = event.y()
            pixmap = self.canvas.pixmap()
            painter = QPainter(pixmap)
            
            if self.font:
                font = self.font
                font.setPointSize(18)
                painter.setFont(font)
                
            font_metrics = QFontMetrics(painter.font())
            text_width = font_metrics.width(text)
            text_height = font_metrics.height()
            center_x = x - text_width // 2
            center_y = y + text_height // 2
            painter.setPen(QColor(Qt.black))
            painter.drawText(center_x, center_y, text)
            painter.end()
            self.canvas.setPixmap(pixmap)

class dockRightSide(QDockWidget):
    def __init__(self, pixmap_widget, parent=None):
        super().__init__(parent)
        self.pixmap_widget = pixmap_widget
        self.initUI()

    def initUI(self):
        layout = QVBoxLayout()
        container = QWidget()

        self.font_list_widget = QListWidget()
        self.font_list_widget.setFixedHeight(200)
        layout.addWidget(self.font_list_widget)
        
        self.font_list_widget.addItems(QFontDatabase().families())
        self.font_list_widget.currentTextChanged.connect(self.set_text_font)
        
        self.font_status = QStatusBar()
        layout.addWidget(self.font_status)
        
        self.text_input = QPlainTextEdit()
        self.text_input.setFixedHeight(200)
        layout.addWidget(self.text_input)

        copy_button = QPushButton('Copy')
        copy_button.clicked.connect(self.copy_text)
        layout.addWidget(copy_button)
        
        self.copy_status = QStatusBar()
        layout.addWidget(self.copy_status)
        
        spacer_item = QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Expanding)
        layout.addItem(spacer_item)
        
        container.setLayout(layout)
        self.setWidget(container)
        self.setWindowTitle('Dock Widget')
        self.setAllowedAreas(Qt.RightDockWidgetArea)
        
        self.canvas = self.pixmap_widget.canvas

    def copy_text(self):
        clipboard = QApplication.clipboard()
        text = self.text_input.toPlainText()
        clipboard.setText(text)
        self.copy_status.showMessage('Text copied!')
        QTimer.singleShot(1000, self.copy_status.clearMessage)
        
    def set_text_font(self, font):
            current_font = self.font_list_widget.currentItem().text()
            self.font_status.showMessage('Font Selected: {}'.format(current_font))
            self.pixmap_widget.font = QFont(current_font)
            pixmap = self.pixmap_widget.canvas.pixmap()
            font = QFont(current_font)
            painter = QPainter(pixmap)
            painter.setFont(font)
            painter.end()
            self.pixmap_widget.canvas.setPixmap(pixmap)
                        
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Simple Manga Editor - Tugas Pemrograman Visual Week 11 & Week 12')
        self.setGeometry(50, 50, 1250, 650)
        self.showMaximized()

        splitter = QSplitter(self)
        tree_view = QTreeView()
        self.setupTreeView(tree_view)

        pixmap = PixMapT()
        dock_widget = dockRightSide(pixmap)

        splitter.addWidget(tree_view)
        splitter.addWidget(pixmap)
        splitter.addWidget(dock_widget)

        splitter.setStretchFactor(0, 1)
        splitter.setStretchFactor(1, 200)
        splitter.setStretchFactor(2, 1)

        self.setCentralWidget(splitter)

        tree_view.setDragEnabled(True)
        pixmap.setAcceptDrops(True)

        toolbar = QToolBar(self)
        self.addToolBar(toolbar)

        toggle_action = QAction("<<", self)
        toggle_action.setCheckable(True)
        toggle_action.setChecked(True)
        toggle_action.triggered.connect(lambda checked: self.toggle_tree_view(checked, toggle_action, splitter))
        toolbar.addAction(toggle_action)
        
        save_as_action = QAction("Save As", self)
        save_as_action.triggered.connect(self.saveAs)
        toolbar.addAction(save_as_action)

        self.show()

    def saveAs(self):
        pixmap = PixMapT()
        pixmap.saveAs()

    def toggle_tree_view(self, checked, toggle_action, splitter):
        tree_view = splitter.widget(0)
        if checked:
            tree_view.show()
            toggle_action.setText("<<")
        else:
            tree_view.hide()
            toggle_action.setText(">>")
            
    def setupTreeView(self, tree_view):
        model = QFileSystemModel()
        current_path = QDir.currentPath()
        model.setRootPath(current_path)
        img_index = model.index(current_path + "/img")
        
        tree_view.setModel(model)
        tree_view.setRootIndex(img_index)
        tree_view.expandAll()
        tree_view.setDragDropMode(QTreeView.DragDrop)
        tree_view.setSelectionMode(QTreeView.ExtendedSelection)
        tree_view.setDragEnabled(True)
        tree_view.setAcceptDrops(False)
        tree_view.setDropIndicatorShown(True)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec_())
