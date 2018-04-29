import sys
from PyQt5.QtWidgets import QWidget, QApplication, QLabel
from PyQt5.QtGui import QPixmap


# noinspection PyArgumentList
from medicalShop.medshow import MedShow


class MedicalShop(QWidget,MedShow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        label = QLabel(self)
        pixmap = QPixmap('img/image.png')
        label.setPixmap(pixmap)
        # Optional, resize window to image size
        # self.resize(pixmap.width(), pixmap.height())
        self.setGeometry(300, 150, 500, 500)
        self.setWindowTitle('MedicalShop')
        self.show()


if __name__ == '__main__':
    app: QApplication = QApplication(sys.argv)
    ex = MedicalShop()
    sys.exit(app.exec_())
