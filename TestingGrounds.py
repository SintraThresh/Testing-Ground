from PyQt5.QtWidgets import QApplication, QPushButton, QLabel, QWidget, QVBoxLayout, QGridLayout, QMessageBox

def maths():
    apple = 1
    banana = 2
    both = banana + apple
    return str(both)

app = QApplication([])
window =  QWidget()
window.setGeometry(500,200,800,400)
button1 =  QPushButton("Math")
button2 = QPushButton("Clear")
layout = QGridLayout()
label = QLabel('The answer is ' + maths())
def on_button_clicked():
    layout.addWidget(label, 0, 1)
    label.show()
button1.clicked.connect(on_button_clicked)
def clear_button():
    label.hide()
button2.clicked.connect(clear_button)


layout.addWidget(button1, 0, 0)
layout.addWidget(button2, 1, 0, 1, 2)
button1.resize(100,32)

window.setLayout(layout)
window.show()
app.exec_()