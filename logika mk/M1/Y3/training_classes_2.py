#підключення бібліотек
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *



def show_win():
    win = QMessageBox()
    win.setText("WIN")
    win.exec_()


def show_lose():
    lose = QMessageBox()
    lose.setText("Lose")
    lose.exec_()

#створення додатка і головного вікна
app = QApplication([])
main_win = QWidget()
main_win.setWindowTitle("Конкурс від Crazy People")
main_win.resize(400,200)
#створення віджетів головного вікна
quw = QLabel("В якому році канал отримав 'золоту кнопку' від YouTube?") #запитання
anw1= QRadioButton("2020")
anw2 = QRadioButton("2015")
anw3 = QRadioButton("2010")
anw4 =QRadioButton("2005")
#розташування віджетів по лейаутам
main_line = QVBoxLayout()
line1= QHBoxLayout()
line2=QHBoxLayout()
line0= QHBoxLayout()

line0.addWidget(quw, alignment=Qt.AlignCenter)
line1.addWidget(anw1, alignment=Qt.AlignCenter)
line1.addWidget(anw2, alignment=Qt.AlignCenter)
line2.addWidget(anw3, alignment=Qt.AlignCenter)
line2.addWidget(anw4, alignment=Qt.AlignCenter)

main_line.addLayout(line0)
main_line.addLayout(line1)
main_line.addLayout(line2)


main_win.setLayout(main_line)

anw1.clicked.connect(show_lose)
anw4.clicked.connect(show_lose)
anw3.clicked.connect(show_lose)
anw2.clicked.connect(show_win)

#обробка натискань на перемикачі

#відображення вік
main_win.show()
app.exec_()