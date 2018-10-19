import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QDesktopWidget, QHBoxLayout, QPushButton, QWidget
from PyQt5.QtGui import QIcon


class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.resize(800, 600)
        self.status = self.statusBar()
        self.status.showMessage("This is status tip", 5000)
        self.setWindowTitle("PyQt window example")
        self.closeButton = QPushButton('close window')
        self.closeButton.clicked.connect(self.onButtonClick)

        layout = QHBoxLayout()
        layout.addWidget(self.closeButton)

        main_frame = QWidget()
        main_frame.setLayout(layout)
        self.setCentralWidget(main_frame)


        self.center()


    def center(self):
        screen = QDesktopWidget().screenGeometry()
        size = self.geometry()
        self.move((screen.width() - size.width()) / 2, (screen.height() - size.height()) / 2)

    def onButtonClick(self):
        sender = self.sender()
        print(sender)
        qa = QApplication.instance()
        qa.quit()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    # app.setWindowIcon()
    form = MainWindow()
    form.show()
    sys.exit(app.exec_())

