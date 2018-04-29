import sys

import PyQt5
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QWidget, QTableWidget, QTableWidgetItem, QVBoxLayout

#Show Medicine
class MedShow(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(300, 50, 600, 600)
        self.setWindowTitle('MedicalShop')
        self.createTable()
        # Add box layout, add table to box layout and add box layout to widget
        self.layout = QVBoxLayout()
        self.layout.addWidget(self.tableWidget)
        self.setLayout(self.layout)
        self.show()

    def createTable(self):
        file = open("doc/meds.txt", "r")
        self.tableWidget = QTableWidget()
        self.tableWidget.setRowCount(100)
        self.tableWidget.setColumnCount(5)
        self.tableWidget.setHorizontalHeaderLabels(['Name', 'Concentration', 'Type', 'Quantity', 'Price'])
        i = j = 0
        for line in file:
            for word in line.split():
                self.tableWidget.setItem(i, j, QTableWidgetItem(word))
                self.tableWidget.move(i, j)
                j = j + 1
        file.close()
        self.tableWidget.doubleClicked.connect(self.on_click)

    @pyqtSlot()
    def on_click(self):
        print('\n')
        for currentQTableWidgetItem in self.tableWidget.selectedItems():
            print(currentQTableWidgetItem.row(),
                  currentQTableWidgetItem.column(),
                  currentQTableWidgetItem.text())


if __name__ == '__main__':
    app: PyQt5.QtWidgets.QApplication = PyQt5.QtWidgets.QApplication(sys.argv)
    ex = MedShow()
    sys.exit(app.exec_())
