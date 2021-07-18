from pandas.core.frame import DataFrame
import requests
import pandas as pd

#1. read base currencies from Huobi API and store them into list base_currencies

base = requests.get('https://api.huobi.pro/v1/common/symbols')
data = pd.DataFrame(base.json()['data'])
base_currencies = data['symbol'][data['state']=='online'].tolist()


#2. Querring Huobi API for histroic Kline of each base currency and store closing prices and daily volatility into list Daily_close_price and list Daily_volatility
one_day_return = pd.DataFrame()
volatility = pd.DataFrame()
for i in base_currencies:
    r = requests.get('https://api.huobi.pro/market/history/kline?period=1day&size=200&symbol='+i)
    print('https://api.huobi.pro/market/history/kline?period=1day&size=200&symbol='+i)
    r

    for j in r.json()['data']:
        one_day_return.at[i,j['id']] = (j['close'])
        volatility.at[i,j['id']] = ((j['high']-j['low'])/j['low'])
    
one_day_return.to_csv('one_day_return.csv')
volatility.to_csv('volatility.csv')


