import sys
import PyQt5
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QWidget, QLabel, QPushButton, QTextEdit, QDialog, QTableWidget
from PyQt5.QtWidgets import QTableWidgetItem, QVBoxLayout

#Search Medicine
class SrhMed(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(300, 50, 600, 600)
        self.setWindowTitle('MedicalShop')
        self.l = QLabel(self)
        self.l.setText('Enter the name to be search')
        self.l.move(150, 10)
        self.t = QTextEdit(self)
        self.t.setFixedHeight(23)
        self.t.move(150,25)
        self.b = QPushButton("Search", self)
        self.b.setCheckable(True)
        self.b.clicked.connect(self.search)
        self.b.move(425, 25)

        self.show()

    @pyqtSlot()
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

    def createTable(self):
        file = open("doc/meds.txt", "r")
        self.tableWidget = QTableWidget()
        self.tableWidget.setColumnCount(5)
        self.tableWidget.setRowCount(100)
        self.tableWidget.setHorizontalHeaderLabels(['Name', 'Concentration', 'Type', 'Quantity', 'Price'])
        i = j = 0
        for line in file:
            for word in line.split():
                self.tableWidget.setItem(i, j, QTableWidgetItem(word))
                self.tableWidget.move(i, j)
                j = j + 1
        file.close()
        self.tableWidget.doubleClicked.connect(self.on_click)


if __name__ == '__main__':
    app: PyQt5.QtWidgets.QApplication = PyQt5.QtWidgets.QApplication(sys.argv)
    ex = SrhMed()
    sys.exit(app.exec_())
