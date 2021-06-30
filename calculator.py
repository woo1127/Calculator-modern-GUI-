from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import sys, os


def resource_path(relative_path):
    """ Get the absolute path to the resource, works for dev and for PyInstaller """
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)


class Calculator(QWidget):
    def __init__(self):
        super().__init__()
        self.win = None
        self.UI()
        self.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0.091, y1:0.101636, x2:0.991379, y2:0.977," 
        "stop:0 pink, stop:1 rgba(255, 240, 255, 255));")
        self.setWindowTitle('Calulator')
        
    
    def UI(self):
        self.keyboard = [
                '7', '8', '9', 'DEL', 'AC',
                '4', '5', '6', ' \N{MULTIPLICATION SIGN} ',
                ' \N{DIVISION SIGN} ',
                '1', '2', '3', ' + ', ' - ',
                '0', '00', '.', '='
        ]

        self.output = QLineEdit()
        self.output.setFixedSize(250, 50)
        self.output.setStyleSheet("background-color: white;" 
                                "border-radius: 10px;"
                                "border: 2px solid lightgreen;"
                                "font-size: 16px")
        self.output_text = ''

        container = QVBoxLayout()
        container.setContentsMargins(10, 20, 10, 10)
        container.setSpacing(5)
        container.addWidget(self.output)

        layout = QGridLayout()
        container.addLayout(layout)

        position = 0
        grid = [[i,j] for i in range(4) for j in range(5)]

        for item in self.keyboard:
            self.button = QPushButton(item)
            self.button.clicked.connect(self.key_input)
            self.button.setStyleSheet("QPushButton"
                                    "{"
                                    "border: 1px solid green;"
                                    "border-radius: 20px;"
                                    "background-color : rgba(0, 255, 0, 0.3);"
                                    "}"
                                    "QPushButton::hover"
                                    "{"
                                    "background-color : yellow;"
                                    "}")
            if item != '=':
                layout.addWidget(self.button, grid[position][0], grid[position][1])
                self.button.setFixedSize(40, 40)
            else:
                layout.addWidget(self.button, 3, 3, 1, 2)
                self.button.setFixedSize(90, 40)
            position += 1

        self.setLayout(container)
    

    def key_input(self):
        text = self.sender().text()

        try:
            if text == '=':
            
                if '\N{MULTIPLICATION SIGN}' in self.output_text:
                    self.output_text = self.output_text.replace(' \N{MULTIPLICATION SIGN} ', ' * ')
                if '\N{DIVISION SIGN}' in self.output_text:
                    self.output_text = self.output_text.replace(' \N{DIVISION SIGN} ', ' / ')
                if self.output_text[0] == '0':
                    self.output_text = self.output_text.replace('0', '')
                
                self.output_text = str(eval(self.output_text))

            elif text == 'DEL':
                self.output_text = self.output_text[:-1]
            elif text == 'AC':
                self.output_text = ''
                self.output.setPlaceholderText('')
            elif text == '00':
                if self.win == None:
                    self.win = MainWindow()
                self.win.show()
            else:
                self.output_text += text
        
            self.output.setText(self.output_text)   

        except SyntaxError and IndexError:
            self.output.setPlaceholderText('Please enter number first')
        except ZeroDivisionError:
            self.output.setPlaceholderText("cannot")
        

class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.scroll = QScrollArea()             
        self.widget = QWidget()                 
        self.vbox = QVBoxLayout()               

        object = QTextEdit()
        object.setText()
        self.vbox.addWidget(object)

        self.widget.setLayout(self.vbox)
        self.scroll.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.scroll.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.scroll.setWidgetResizable(True)
        self.scroll.setWidget(self.widget)

        self.setCentralWidget(self.scroll)

        self.setGeometry(100, 100, 500, 500)
        self.setWindowTitle('Scroll Area Demonstration')
        

def main():
    app = QApplication(sys.argv)
    win = Calculator()
    win.show()
    sys.exit(app.exec())


main()


