from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout
import random

app = QApplication([])
window = QWidget()
window.resize(400,200)
window.setWindowTitle('Лотерея')
text = QLabel('Нажми, чтобы участвовать')
q_mark_1 = QLabel('?')
q_mark_2 = QLabel('?')
button = QPushButton('Испытать удачу')
line = QVBoxLayout()
line.addWidget(text, alignment= Qt.AlignCenter)
line.addWidget(q_mark_1, alignment= Qt.AlignCenter)
line.addWidget(q_mark_2, alignment= Qt.AlignCenter)
line.addWidget(button, alignment= Qt.AlignCenter)
window.setLayout(line)

def winner():
    num_1 = random.randint(0,9)
    num_2 = random.randint(0,9)
    if num_1 == num_2:
        text.setText('Вы выиграли!')
        q_mark_1.setText(str(num_1))
        q_mark_2.setText(str(num_2))
        button.setText('Сыграйте снова')
    else:
        text.setText('Вы проиграли!')
        q_mark_1.setText(str(num_1))
        q_mark_2.setText(str(num_2))
        button.setText('Сыграйте снова')
button.clicked.connect(winner)       


window.show()
app.exec_()