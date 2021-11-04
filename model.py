class Question:

    def __init__(self, question, category, type, difficulty, correct_answer, incorrect_answers):
        self.question = question
        self.type = type
        self.category = category
        self.difficulty = difficulty
        self.correct_answer = correct_answer
        self.incorrect_answers = incorrect_answers


class ScoreBoard:
    good: int = 0
    bad: int = 0

    bad_questions = []

    def AddBadQuestions(self, question: Question, answer: str):
        """

        :type answer: object
        """
        self.bad_questions.append(question)


class CheckAnswer:
    @staticmethod
    def Check(self, question: Question, answer: str):
        if answer.lower() == question.answer.lower():
            return True
        else:
            return False
