class Question:

    def __init__(self, phrase, answer):
        self.phrase = phrase
        self.answer = answer


class ScoreBoard:
    good: int = 0
    bad: int = 0

    bad_questions = {}

    def AddBadQuestions(self, question: Question, answer: str):
        """

        :type answer: object
        """
        self.bad_questions[question]=answer


class CheckAnswer:

    def Check(self, question:Question, answer):
        if answer == question.answer:
            return True
        else:
            return False


