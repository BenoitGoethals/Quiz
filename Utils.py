import json

import model
import requests


# https://opentdb.com/api_config.php

class WebApi:
    def __init__(self):
        pass



    @staticmethod
    def questions():
        response = requests.get("https://opentdb.com/api.php?amount=10&category=9&difficulty=easy")
        data = response.json()
        strData = json.loads(data)

        return strData
