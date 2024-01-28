from PyQt5.QtWidgets import *
from memo_app import *
from PyQt5.QtCore import *

width, height = 600, 500
win_card = QWidget()
win_card.resize(width, height)
win_card.move(300, 300)
win_card.setWindowTitle("Memory Card")

btn_sleep= QPushButton("Відпочити")
box_minutes = QSpinBox()
box_minutes.setValue(30)
label_box_min = QLabel()
label_box_min.setText("хвилин")

btn_menu = QPushButton("Меню")
btn_OK= QPushButton("Відповісти")

ln_question = QLabel(" ")

RadioGroupBox = QGroupBox("Варіанти відповідей")
RadioGroupBox = QButtonGroup()
btn_1 = QRadioButton("")
btn_2 = QRadioButton("")
btn_3 = QRadioButton("")
btn_4 = QRadioButton("")

RadioGroupBox.addButton(btn_1)
RadioGroupBox.addButton(btn_2)
RadioGroupBox.addButton(btn_3)
RadioGroupBox.addButton(btn_4)

AnsGroupBox = QGroupBox("Результати тесту")
lb_result = QLabel('')
lb_correct= QLabel('')
layout_ans1 = QHBoxLayout()
layout_ans2 = QVBoxLayout()
layout_ans3 = QVBoxLayout()

layout_ans2.addWidget(btn_1)
layout_ans2.addWidget(btn_2)
layout_ans3.addWidget(btn_3)
layout_ans3.addWidget(btn_4)

layout_ans1.addLayout(layout_ans2)
layout_ans1.addLayout(layout_ans3)

RadioGroupBox.set(layout_ans1)

layout_res= QVBoxLayout()
layout_res.addWidget(lb_result, alignment=(Qt.AlignLeft | Qt.AlignTop))
layout_res.addWidget(lb_correct, alignment= Qt.AlignCenter, stretch=2)

AnsGroupBox.setLayout(layout_res)
AnsGroupBox.hide()



layout_ok = QBoxLayout()
layout_ok.addWidget(btn_OK, stretch=2)








win_card.show()
app.exec_()

