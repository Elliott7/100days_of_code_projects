"""
Project Number Seventeen - Question Quiz
The point of this project was to create a quiz using classes
"""

question_data = [
    {"text": "A slug's blood is green.", "answer": "True"},
    {"text": "The loudest animal is the African Elephant.", "answer": "False"},
    {"text": "Approximately one quarter of human bones are in the feet.", "answer": "True"},
    {"text": "The total surface area of a human lungs is the size of a football pitch.", "answer": "True"},
    {"text": "In West Virginia, USA, if you accidentally hit an animal with your car, "
             "you are free to take it home to eat.", "answer": "True"},
    {"text": "In London, UK, if you happen to die in the House of Parliament, "
             "you are entitled to a state funeral.", "answer": "False"},
    {"text": "It is illegal to pee in the Ocean in Portugal.", "answer": "True"},
    {"text": "You can lead a cow down stairs but not up stairs.", "answer": "False"},
    {"text": "Google was originally called 'Backrub'.", "answer": "True"},
    {"text": "Buzz Aldrin's mother's maiden name was 'Moon'.", "answer": "True"},
    {"text": "No piece of square dry paper can be folded in half more than 7 times.", "answer": "False"},
    {"text": "A few ounces of chocolate can to kill a small dog.", "answer": "True"}
]


class Question:

    def __init__(self, text, answer):
        self.text = text
        self.answer = answer


class QuestionBank:

    def __init__(self, q_list):
        self.bank = q_list
        self.question_number = 0
        self.score = 0

    def add_question(self, question):
        self.bank.append(question)

    def display(self):
        print(f"Q.{self.question_number+1}: {self.bank[self.question_number].text} (True/False)")

    def increment(self):
        self.question_number += 1

    def compare(self):
        user_answer = input()
        if user_answer.title() == self.bank[self.question_number].answer:
            self.score += 1
            self.question_number += 1
            print("You are correct")
        else:
            self.question_number += 1
            print("You are incorrect")

    def still_questions(self):
        try:
            self.bank[self.question_number]
            return True
        except IndexError:
            print("There are no more questions. The game is now ending")
            return False


def main():
    bank = []
    for i in range(len(question_data) - 1):
        temp = Question(question_data[i]['text'], question_data[i]['answer'])
        bank.append(temp)

    question_bank = QuestionBank(bank)
    while True:
        question_bank.display()
        question_bank.compare()
        print(f"Your score stands at: {question_bank.score}")
        if question_bank.still_questions():
            continue
        else:
            break


if __name__ == "__main__":
    main()
