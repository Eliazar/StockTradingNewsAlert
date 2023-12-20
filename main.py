from twilioManager import twiliomanager
from stockTradeManager import stockmanager
from newsManager import newsmanager

smanager = stockmanager.StockTradeManager()
recentData = smanager.getLastUpdatedData()
yesterdayData = smanager.getPreviousDayData()

todayClose = float(recentData.get("4. close"))
yesterdayClose = float(yesterdayData.get("4. close"))

incresePercentage = (todayClose / yesterdayClose) - 1
incresePercentage = round(incresePercentage, 2) * 100

nmanager = newsmanager.NewsManager()
relevantNew = nmanager.getRelevantNews()

tmanager = twiliomanager.TwilioManager()

if (incresePercentage > 0.1):
    tmanager.message(
        f"El precio de las acciones 🔼 un {incresePercentage}.\nNoticia relevante: {relevantNew}")
elif (incresePercentage < -0.1):
    tmanager.message(
        f"El precio de las acciones 🔽 un {incresePercentage}.\nNoticia relevante: {relevantNew}")
else:
    tmanager.message(
        f"El precio de las acciones se mantiene. \nNoticia relevante: {relevantNew}")
