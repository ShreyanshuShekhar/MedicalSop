import sys
import PyQt5
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QWidget, QLabel, QPushButton, QTextEdit, QDialog, QTableWidget
from PyQt5.QtWidgets import QTableWidgetItem, QVBoxLayout
from PyQt5.QtGui import QPixmap

#Search Medicine
class SrhMed(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(300, 30, 635, 635)
        self.setWindowTitle('MedicalShop')
        self.li = QLabel(self)
        pixmap = QPixmap('img/5.jpg')
        self.li.setPixmap(pixmap)
        self.l = QLabel(self)
        self.l.setText('Enter the medicine to be search')
        self.l.move(200, 70)
        self.t = QTextEdit(self)
        self.t.setFixedHeight(23)
        self.t.move(200,90)
        self.b = QPushButton("Search", self)
        self.b.setCheckable(True)
        self.b.clicked.connect(self.search)
        self.b.move(480, 90)
        self.b1 = QPushButton("Medicine List", self)
        self.b1.setCheckable(True)
        self.b1.clicked.connect(self.on_click)
        self.b1.setFixedHeight(30)
        self.b1.setFixedWidth(300)
        self.b1.setStyleSheet("background-color: #FF4500")
        self.b1.move(200, 130)
        self.b2 = QPushButton("Medicines Bought", self)
        self.b2.setCheckable(True)
        self.b2.clicked.connect(self.click())
        self.b2.setFixedHeight(30)
        self.b2.setFixedWidth(300)
        self.b2.setStyleSheet("background-color: #FF4500")
        self.b2.move(200, 130)
        self.show()

    @pyqtSlot()
    def on_click(self):
        self.tb = medshow()
        self.tb.createTable()

    def click(self):
        file1 =open("doc/med.txt", "r")
        for line in file1:
            if file1

    def search(self):
        source = self.sender()
        if source.text() == ' ':
            self.d = QDialog('no input', self)
        else:
            self.createTable()
            # Add box layout, add table to box layout and add box layout to widget
            self.layout = QVBoxLayout()
            self.layout.addWidget(self.tableWidget)
            self.setLayout(self.layout)
            self.show(self)

    '''def createTable(self):
        file = open("doc/meds.txt", "r")
        for line in file:
            for word in line.split():
                if(word)
                self.tableWidget.setItem(i, j, QTableWidgetItem(word))
                self.tableWidget.move(i, j)
                j = j + 1
        file.close()
        self.tableWidget = QTableWidget()
        self.tableWidget.setColumnCount(5)
        self.tableWidget.setRowCount(100)
        self.tableWidget.setHorizontalHeaderLabels(['Name', 'Concentration', 'Type', 'Quantity', 'Price'])
        self.tableWidget.doubleClicked.connect(self.on_click)'''


if __name__ == '__main__':
    app: PyQt5.QtWidgets.QApplication = PyQt5.QtWidgets.QApplication(sys.argv)
    ex = SrhMed()
    sys.exit(app.exec_())
