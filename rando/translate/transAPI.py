import requests, os, sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot

languages = {
    'Afrikaans' : 'af',
    'Czech' : 'cs',
    'Dutch' : 'nl',
    'French' : 'fr',
    'English' : 'en',
    'Chinese (Simplified)' : 'zh-CN',
    'Spanish' : 'es'
}

class App(QMainWindow):
    def __init__(self):
        super().__init__()
        self.title = "Translate API"
        self.left = 100
        self.top = 100
        self.width = 400
        self.height = 140
        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        
        # Create the textbox
        self.textbox = QLineEdit(self)
        self.textbox.move(20, 20)
        self.textbox.resize(280, 40)
        
        # Language selection
        
        # From choice
        self.fromLanguage = QComboBox(self)
        self.fromLanguage.addItem('detect')
        for i in languages:
            self.fromLanguage.addItem(languages[i])        
        self.fromLanguage.move(20, 100)
        self.fromLabel = QLabel(self)
        self.fromLabel.move(30, 70)
        self.fromLabel.setText('From:')

        # To choice
        self.toLanguage = QComboBox(self)
        for i in languages:
            self.toLanguage.addItem(languages[i])
        self.toLanguage.move(140,100)
        self.toLabel = QLabel(self)
        self.toLabel.move(150, 70)
        self.toLabel.setText('To:')

        # Create a button
        self.button = QPushButton('Show text', self)
        self.button.move(260, 95)

        # Connect the button to the function 'on_click'
        self.button.clicked.connect(self.on_click)
        self.show()

    @pyqtSlot()
    def on_click(self):
        textboxValue = self.textbox.text()
        url = "https://google-translate1.p.rapidapi.com/language/translate/v2"
        # os.system('cls' if os.name =='nt' else 'clear')
        phrase = textboxValue
        for i in range(len(phrase)):
            if phrase[i]==' ':
                phrase[i]=='%20'
        targ=self.toLanguage.currentText()
        src = ''
        if self.fromLanguage.currentText() == 'detect':
            src = ""
        else: 
            src = self.fromLanguage.currentText()
        print(f'source is {src}')
        payload = f"q={phrase}&target={targ}&source={src}"
        headers = {
        	"content-type": "application/x-www-form-urlencoded",
        	"Accept-Encoding": "application/gzip",
        	"X-RapidAPI-Key": "93295dd330msh36f1be01e7edc34p17282ejsnc478a05c162e",
        	"X-RapidAPI-Host": "google-translate1.p.rapidapi.com"
        }
        response = requests.request("POST", url, data=payload, headers=headers)
        data_json = response.json()
        trans = data_json['data']
        text = trans['translations']
        transFinal = text[0]['translatedText']

        # print(transFinal)


        QMessageBox.question(self, 'Translated -', f'The translated value is: {transFinal}', QMessageBox.Ok, QMessageBox.Ok)
        self.textbox.setText("")


if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())