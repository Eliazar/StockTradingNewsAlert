import requests
import os

BASE_URL = "https://newsapi.org/v2/everything"
API_KEY = os.environ.get("NEWS_API_KEY")


class NewsManager:
    __parameters = {
        "q": "Kimberly-Clark",
        "language": "en",
        "searchIn": "title",
        "apiKey": API_KEY,
    }

    def __init__(self):
        self.response = requests.get(BASE_URL, params=self.__parameters)
        self.response.raise_for_status()

    def printResponse(self):
        print(self.response.json())

    def getRelevantNews(self):
        data = self.response.json()
        data = data.get("articles")[0]
        return data.get("title")
