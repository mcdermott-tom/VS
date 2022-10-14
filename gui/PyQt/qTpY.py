import sys
# QtWidgets contains all major widgets we'll use
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QMessageBox, QGroupBox

def dialog():
    mbox = QMessageBox()

    mbox.setText("You have been noticed, \nnow stop before you're destroyed.")
    mbox.setDetailedText("That is a promise.")
    mbox.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)

    mbox.exec_()

if __name__ =='__main__':
    # must create object of QApplication class for PyQt
    app = QApplication(sys.argv)
    w = QWidget()
    w.resize(300,300)
    w.setWindowTitle("ASCP")
    docs = QGroupBox(w)
    
    label = QLabel(docs)
    label.setText("I AM GOD")
    label.move(100, 130)
    label.show()

    btn = QPushButton(docs)
    btn.setText('Beheld')
    btn.move(110, 140)
    btn.show()
    btn.clicked.connect(dialog)






    w.show()
    sys.exit(app.exec_())