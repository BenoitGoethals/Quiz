# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import model
import Utils
import random
from prettytable import PrettyTable


def print_table(_questions):
    x = PrettyTable()

    x.field_names = ["question", "category", "type", "difficulty", "correct_answer"]
    for q in _questions:
        x.add_row([q.question, q.category, q.type, q.difficulty, q.correct_answer])

    print(x)


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')
    questions = Utils.WebApi.questions()
    scoreBoard = model.ScoreBoard()
    print_table(questions)
    running = True
    counter = 1
    while running and counter != len(questions):
        question: model.Question = questions[random.randint(1, len(questions) - 1)]
        answer = input(f"{counter}) What is answer  {question.question} :")
        if answer == "x":
            running = False
        elif question.correct_answer == answer:
            print("Good Answer")
            scoreBoard.good += 1
        elif question.correct_answer != answer:
            print("Bad Answer")
            scoreBoard.bad += 1
            scoreBoard.AddBadQuestions(question, answer)
        counter += 1
print(f"Good Question {scoreBoard.good}")
print(f"Bad Question {scoreBoard.bad}")
print("Bad")
print_table(scoreBoard.bad_questions)
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
