"""
Project Thirty-Four - Quizzler App
API driven quiz app using Tkinter GUI
"""

import requests as rq
import html
from tkinter import *

THEME_COLOR = "#375362"
NUMBER_OF_QUESTIONS = 10


class Question:

    def __init__(self, q_text, q_answer):
        self.text = q_text
        self.answer = q_answer


class QuizBrain:

    def __init__(self, q_list):
        self.question_number = 0
        self.score = 0
        self.question_list = q_list
        self.current_question = None

    def still_has_questions(self):
        return self.question_number < len(self.question_list)

    def next_question(self):
        self.current_question = self.question_list[self.question_number]
        self.question_number += 1
        q_text = html.unescape(self.current_question.text)
        return f"Q.{self.question_number}: {q_text} (True/False): "

    def check_answer(self, user_answer):
        correct_answer = self.current_question.answer
        if user_answer.lower() == correct_answer.lower():
            self.score += 1
            return True
        else:
            return False


class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        self.score_label = Label(text='Score: 0', fg='white', bg=THEME_COLOR)
        self.score_label.grid(row=0, column=1)
        self.score = 0

        self.canvas = Canvas(width=300, heigh=250, bg='white')
        self.question_text = self.canvas.create_text(
            150,
            125,
            width=280,
            text='Test',
            fill=THEME_COLOR,
            font=("Arial", 17, 'italic')
        )
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)

        true_image = PhotoImage(file='true.png')
        self.true_button = Button(image=true_image, highlightthickness=0, command=self.true_pressed)
        self.true_button.grid(row=2, column=0)

        false_image = PhotoImage(file='false.png')
        self.false_button = Button(image=false_image, highlightthickness=0, command=self.false_pressed)
        self.false_button.grid(row=2, column=1)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        if self.quiz.still_has_questions():
            self.canvas.config(bg='white')
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text, text="You've reached the end of the quiz")
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")


    def true_pressed(self):
        y = self.quiz.check_answer('True')
        self.give_feedback(y)

    def false_pressed(self):
        x = self.quiz.check_answer('False')
        self.give_feedback(x)

    def score_increment(self):
        self.score += 1
        self.score_label['text'] = f'Score: {self.score}'

    def give_feedback(self, ans):
        if ans:
            self.canvas.config(bg='green')
            self.score_increment()
        else:
            self.canvas.config(bg='red')
        self.window.after(1000, self.get_next_question)


question_bank = []
parameters = {
    'amount': NUMBER_OF_QUESTIONS,
    'type': 'boolean'
}
api_endpoint = f'https://opentdb.com/api.php'

response = rq.get(api_endpoint, params=parameters)
data = response.json()
print(data)
for i in range(NUMBER_OF_QUESTIONS):
    question = data['results'][i]['question']
    answer = data['results'][i]['correct_answer']
    new_question = Question(question, answer)
    question_bank.append(new_question)

print(question_bank)

quiz = QuizBrain(question_bank)
quiz_ui = QuizInterface(quiz)


print("You've completed the quiz")
print(f"Your final score was: {quiz.score}/{quiz.question_number}")
