import requests
import os

BASE_URL = "https://www.alphavantage.co/query?"
API_KEY = os.environ.get("ALPHA_VANTAGE_KEY")


class StockTradeManager:
    __parameters = {
        "function": "TIME_SERIES_DAILY",
        "symbol": "KMB",
        "apikey": API_KEY,
    }

    def __init__(self):
        self.response = requests.get(BASE_URL, params=self.__parameters)
        self.response.raise_for_status()

    def printResponse(self):
        print(self.response.json())

    def getLastUpdatedData(self):
        data = self.response.json().get("Time Series (Daily)")
        keys = list(data.keys())
        return data[keys[0]]

    def getPreviousDayData(self):
        data = self.response.json().get("Time Series (Daily)")
        keys = list(data.keys())
        return data[keys[1]]
