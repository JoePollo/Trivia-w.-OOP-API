from requests import get as reqGet
from html import unescape
class Questions:
    def __init__(self):
        self.gameLength = 10
        self.apiToken = reqGet(url = "https://opentdb.com/api_token.php?command=request")
        self.questionsAPIResponse = reqGet(url = f"https://opentdb.com/api.php?amount={self.gameLength}&type=boolean&token={self.apiToken.json()['token']}")
        self.questionsDictionary = self.dictionaryConstructor()
        self.quizLength = len(self.questionsDictionary["question"])-1


    def dictionaryConstructor(self):
        qDictionary = {
            "question": [],
            "answer": []
        }
        for i in range(len(self.questionsAPIResponse.json()["results"])):
            qDictionary["question"].append(unescape(self.questionsAPIResponse.json()["results"][i]["question"]))
            qDictionary["answer"].append(unescape(self.questionsAPIResponse.json()["results"][i]["correct_answer"]))
        return qDictionary

    def questionGenerator(self) -> tuple:
        if self.quizLength >= 0:
            question = self.questionsDictionary["question"][self.quizLength]
            answer = self.questionsDictionary["answer"][self.quizLength]
            self.quizLength -= 1
            return (question, answer)