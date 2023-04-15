#cjxvdfjnv;/sdnbvjdsnvsdkn
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout, QHBoxLayout
from random import *
app = QApplication([])
main_win = QWidget()
main_win.setWindowTitle('Определитель победителя')
main_win.resize(400, 200)
button = QPushButton('Сгенерировать')
text = QLabel('Нажми, чтобы узнать победителя')
winner = QLabel('?')

count = 0
def show_winner():
    
    global count,line2
    count +=1
    if count == 1:
        winner.setText("111")
    elif count %3 == 1:
        winner.setText("100")
    
    else:
        num = str(randint(0,100))
        winner.setText(num)
    
        
     
    

button.clicked.connect(show_winner)


line = QVBoxLayout()

line.addWidget(button, alignment = Qt.AlignCenter)
line.addWidget(winner, alignment = Qt.AlignCenter)
line.addWidget(text, alignment = Qt.AlignCenter)
main_win.setLayout(line)

main_win.show()
app.exec_()




























'''
class Button():
    def __init__(self, title_text, x_num, y_num):
        self.title = title_text
        self.x = x_num
        self.y = y_num
        self.appearance = True
    def hide(self):
        self.appearance = False
    def show(self):
        self.appearance = True
    def print_status(self):
        print('Данные о виджете:')
        print(self.title, self.x, self.y, self.appearance)

ok_button = Button('ok', 100, 100)
ok_button.print_status()
ok_button.hide()
ok_button.print_status()

class Application():
    def __init__(self, title_text, description_text, volume_num):
        self.title = title_text
        self.description = description_text
        self.volume = volume_num
        self.SPISOK = [123123,23423,5645654]
    def print_info(self):
        print('Приложение', self.title)
        print('Описание:', self.description)
        print('Размер приложения:', self.volume)
        print(self.SPISOK)
more = Application('kfkfkf','rjjhtbrbh',6785)
more.print_info()
'''
