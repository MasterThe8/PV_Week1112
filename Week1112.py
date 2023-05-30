import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

class PixMap(QLabel):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setAcceptDrops(True)
        self.setScaledContents(True)
        # self.setFixedSize(300, 300)

    def dragEnterEvent(self, event):
        if event.mimeData().hasUrls() or event.mimeData().hasText():
            event.acceptProposedAction()
            
    def dragMoveEvent(self, event):
        event.acceptProposedAction()
        
    def dropEvent(self, event):
        if event.mimeData().hasUrls():
            url = event.mimeData().urls()[0]
            pixmap = QPixmap(url.toLocalFile())
            # if not pixmap.isNull():
            self.setPixmap(pixmap.scaled(self.size(), Qt.AspectRatioMode.KeepAspectRatio, Qt.TransformationMode.SmoothTransformation))
            event.acceptProposedAction()
        # if event.mimeData().hasText():
        #     url = event.mimeData().urls()[0]
        #     pixmap = QPixmap(url.toLocalFile())
        #     if not pixmap.isNull():
        #         self.setPixmap(pixmap.scaled(self.size(), Qt.AspectRatioMode.KeepAspectRatio, Qt.TransformationMode.SmoothTransformation))
        #         event.acceptProposedAction()
            
class dockRightSide(QDockWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        
        self.initUI()

    def initUI(self):
        layout = QVBoxLayout()
        container = QWidget()

        self.list_widget = QListWidget()
        self.list_widget.setFixedHeight(100)
        layout.addWidget(self.list_widget)
        
        
        
        self.list_widget.setDragEnabled(True)  # Aktifkan drag pada QListWidget
        self.list_widget.setDragDropMode(QListWidget.DragOnly)  # Set mode drag-only
        self.list_widget.setSelectionMode(QListWidget.SingleSelection)  # Set mode seleksi tunggal
        self.list_widget.viewport().setAcceptDrops(True)

        copy_button = QPushButton('Copy')
        copy_button.clicked.connect(self.copy_text)
        layout.addWidget(copy_button)

        paste_button = QPushButton('Paste')
        paste_button.clicked.connect(self.paste_text)
        layout.addWidget(paste_button)
        
        spacer_item = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)
        layout.addItem(spacer_item)
        
        container.setLayout(layout)
        self.setWidget(container)
        self.setWindowTitle('Dock Widget')
        self.setAllowedAreas(Qt.RightDockWidgetArea)

    def copy_text(self):
        # Implementasi fungsi copy
        print("Copy")

    def paste_text(self):
        # Implementasi fungsi paste
        print("Paste")
        
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.setWindowTitle('Tugas Pemrograman Visual - Week 11 & Week 12')
        self.setGeometry(50, 50, 1250, 650)
        self.showMaximized()

        splitter = QSplitter(self)

        tree_view = QTreeView()
        self.setupTreeView(tree_view)

        pixmap = PixMap()
        dock_widget = dockRightSide()

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
        
        self.show()

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