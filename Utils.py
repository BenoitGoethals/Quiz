import json

import model
import requests


# https://opentdb.com/api_config.php

class WebApi:
    def __init__(self):
        pass

    # category":"General Knowledge","type":"multiple","difficulty":"easy","question"

    @staticmethod
    def questions():
        response = requests.get("https://opentdb.com/api.php?amount=10&category=9&difficulty=easy")
        data = response.json()
        jtopy = json.dumps(data)
        strData = json.loads(jtopy)

        list_questions=[]

        for q in strData["results"]:
            list_questions.append(model.Question(q["category"], q["type"], q["difficulty"], q["correct_answer"], q["incorrect_answers"]))
        return list_questions
