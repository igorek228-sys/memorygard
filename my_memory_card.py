#создай приложение для запоминания информащии
from PyQt5.QtCore import Qt,QTimer
from PyQt5.QtWidgets import ( QApplication, QWidget, QPushButton, QGroupBox, QLabel, QRadioButton, QVBoxLayout, QButtonGroup)
from random import shuffle
class Question:
    def __init__(self, question, right_answer, wrong1, wrong2, wrong3):
        self.question = question
        self.right_answer = right_answer
        self.wrong1 = wrong1
        self.wrong2 = wrong2
        self.wrong3 = wrong3

questions = [
    Question('шампиньон?', 'Португальский', 'Английский', 'Испанский', 'Бразильский'),
    Question('Какаго цвита гриб Ю,,Ю,Ю,,ЮЮ?', 'Зелёный', 'Красный', 'Белый', 'Синий'),
    Question('скажи правильно бюбююббюбюбюсплмоаирьвыу порсапм', 'не хочу', 'Юрта', 'Иглу', 'щрмкоараоуруоцваро'),
]                                                
                                 
app=QApplication([])
window = QWidget()
window.setWindowTitle("яолррнлоакврПриложжениинеывввввв")
OK = QPushButton("Ответить")
q = QLabel("Вопрос")

RGB = QGroupBox("Варианты ответа")
rb_1 = QRadioButton()
rb_2 = QRadioButton()
rb_3 = QRadioButton()
rb_4 = QRadioButton()

RadioGroup = QButtonGroup()

for btn in (rb_1, rb_2, rb_3, rb_4):
    RadioGroup.addButton(btn)

layout_answers = QVBoxLayout()
for btn in (rb_1, rb_2, rb_3, rb_4):
    layout_answers.addWidget(btn)
RGB.setLayout(layout_answers)

AGB = QGroupBox("результат🎃")
result = QLabel()
Correct = QLabel()
rl = QVBoxLayout()
rl.addWidget(result)
rl.addWidget(Correct)
AGB.setLayout(rl)
AGB.hide()
main = QVBoxLayout()
main.addWidget(q)
main.addWidget(RGB)
main.addWidget(AGB)
main.addWidget(OK)

window.setLayout(main)
answers = [rb_1, rb_2, rb_3, rb_4]

window.correct_answers = 0
window.total_questions = 0

timer = QTimer()
timer.setInterval(1000)
window.time_left = 10

def update_timer():
    window.time_left -= 1       
    OK.setText(f'Ответить ({window.time_left}с)')
    if window.time_left == 0:
        timer.stop()
        check_answer()

def start_timer():
    window.time_left = 10
    timer.start()

def show_questions():
    AGB.hide()
    RGB.show()
    OK.setText('Ответитв (10с)')
    RadioGroup.setExclusive(False)
    for btn in answers:
        btn.setChecked(False)
    RadioGroup.setExclusive(True)
    start_timer()
def show_result():
    RGB.hide()
    AGB.show()
    OK.setText("Следующий вопрос")
    result.setText(f'{result.text()}\n'
    f'Правильных ответов: {window.correct_answers}\n'
    f'Всего вопросов: {window.total_questions}')
    
def ask(question):
    shuffle(answers)
    answers[0].setText(question.right_answer)
    answers[1].setText(question.wrong1)
    answers[2].setText(question.wrong2)
    answers[3].setText(question.wrong3)
    q.setText(question.question)
    Correct.setText(f'Правильный ответ: {question.right_answer}')
    show_questions()

def check_answer():
    timer.stop
    if answers[0].isChecked():
        result.setText('Правильно!')
        window.correct_answers += 1
    else:
        result.setText('Неправильно!')

    window.total_questions += 1
    show_result()

def next_question():
    window.current_question += 1
    if window.current_question >= len(questions):
        window.current_question = 0
    ask(questions[window.current_question])

def click_OK():
    if OK.text() == 'Ответить':
        check_answer()
    else:
        next_question()

window.current_question = -1
OK.clicked.connect(click_OK)
timer.timeout.connect(update_timer)
next_question()
window.show()
app.exec()
































































































