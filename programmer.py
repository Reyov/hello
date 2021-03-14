import sys
from PyQt5.QtWidgets import QApplication, QLabel, QPushButton, QVBoxLayout, QWidget, QFileDialog, QGridLayout
from PyQt5.QtGui import QPixmap
from PyQt5 import QtGui, QtCore
from PyQt5.QtGui import QCursor

# create a dictionary of widgets, with their unique "keys" and [list values]
widgets = {
    "logo": [],
    "button": [],
    "score": [],
    "question": [],
    "answer1": [],
    "answer2": [],
    "answer3": [],
    "answer4": []
}


app = QApplication(sys.argv)
window = QWidget()
window.setWindowTitle("who wants to be a programmeer???")
window.setFixedWidth(1000)
window.move(2500, 200)
window.setStyleSheet("background: #161219;")

grid = QGridLayout()


def clear_widgets():
    for widget in widgets:
        if widgets[widget] != []:
            widgets[widget][-1].hide()
        for i in range(0, len(widgets[widget])):
            widgets[widget].pop()


def show_frame1():
    clear_widgets()
    frame1()


def start_game():
    clear_widgets()
    frame2()


def create_buttons(answer, l_margin, r_margin):
    button = QPushButton(answer)
    button.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
    button.setFixedWidth(485)
    button.setStyleSheet(
        # when using css command, we have to put ; for the command to be executed
        "*{border: 4px solid '#BC006C';" +
        "margin-left: " + str(l_margin) + "px;" +
        "margin-right: " + str(r_margin) + "px;" +
        "color: 'white';" +
        "font-family: 'shanti';" +
        "border-radius: 25px;" +
        "padding: 15px 0;" +
        "margin-top: 20px;}" +
        "*:hover{background: '#BC006C'}"
    )
    button.clicked.connect(show_frame1)
    return button


def frame1():
    # display logo
    image = QPixmap("logo.jpg")
    logo = QLabel()
    logo.setPixmap(image)
    logo.setAlignment(QtCore.Qt.AlignCenter)
    logo.setStyleSheet("margin-top: 100px;")
    widgets["logo"].append(logo)

    # button widget
    button = QPushButton("PLAY")
    button.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
    button.setStyleSheet(
        "*{border: 4px solid '#BC006C';" +
        "border-radius: 45px;" +
        "font-size: 35px;" +
        "color: 'white';" +
        "padding: 25px 0;"
        "margin: 100px 200px;}" +
        "*:hover{background: '#BC006C'};"
    )
    button.clicked.connect(start_game)
    widgets["button"].append(button)

    # -1 is the last object in the list. Best friend in PyQT5. Indx 0 doesn't alwasy work
    grid.addWidget(widgets["logo"][-1], 0, 0, 1, 2)
    grid.addWidget(widgets["button"][-1], 1, 0, 1, 2)
    

def frame2():
    score = QLabel("89")
    score.setAlignment(QtCore.Qt.AlignRight)
    score.setStyleSheet(
        "font-family: 'Shanti';" +
        "font-size: 35px;" +
        "color: 'white';" +
        "padding: 24px 12px 0px 5px;" +
        "margin: 20px 190px 40px 200px;" +
        "background: '#64A314';" +
        "border: 1px solid '#64A314';" +
        "border-radius: 40px;"
    )
    widgets["score"].append(score)

    question = QLabel("placeholder for the question 1 will go here...")
    question.setAlignment(QtCore.Qt.AlignCenter)
    question.setWordWrap(True)
    question.setStyleSheet(
        "font-family: Shanti; font-size: 25px; color: 'white'; padding: 75px;"
    )
    widgets["question"].append(question)

    button1 = create_buttons("answer 1", 85, 5)
    button2 = create_buttons("answer 2", 5, 85)
    button3 = create_buttons("answer 3", 85, 5)
    button4 = create_buttons("answer 4", 5, 85)

    widgets["answer1"].append(button1)
    widgets["answer2"].append(button2)
    widgets["answer3"].append(button3)
    widgets["answer4"].append(button4)

    grid.addWidget(widgets["score"][-1], 0, 1)
    grid.addWidget(widgets["question"][-1], 1, 0, 1, 2)
    grid.addWidget(widgets["answer1"][-1], 2, 0)
    grid.addWidget(widgets["answer2"][-1], 2, 1)
    grid.addWidget(widgets["answer3"][-1], 3, 0)
    grid.addWidget(widgets["answer4"][-1], 3, 1)


frame1()

window.setLayout(grid)

window.show()
sys.exit(app.exec())
