'''
Created on 22 Jun 2023

Course work: To download data from yahoo finance

@author: Sanjjushri

Source:
    
    JSON Request
        https://codehandbook.org/post-json-fastapi/
'''

'''
How to run?

uvicorn app:app --reload
'''


# Import necessary modules
from fastapi import FastAPI
from urllib.request import urlopen
import webbrowser

app = FastAPI()

'''
    http://127.0.0.1:8000/
'''

@app.get("/")
async def abc():
    return {"home": "forex"}

@app.get("/get/forex/data")
def get_forex_data(symbol: str = "EURUSD",
                   interval: str = "1d",
                   range: str = "1y"):

    data_link = "https://query1.finance.yahoo.com/v7/finance/download/{}=X?interval={}&range={}".format(symbol, interval, range)

    url_content = urlopen(data_link)
    data = url_content.read()

    return data

@app.get("/download/data")
def download_data(symbol: str = "EURUSD",
                   interval: str = "1d",
                   range: str = "1y"):

    data_link = "https://query1.finance.yahoo.com/v7/finance/download/{}=X?interval={}&range={}".format(symbol, interval, range)
    
    return webbrowser.open(data_link)


'''
    https://query1.finance.yahoo.com/v7/finance/download/EURUSD=X?interval=1d&range=1y
'''