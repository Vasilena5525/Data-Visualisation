import requests
from bs4 import BeautifulSoup
import json

mystocks=['AMZN', 'AAPL', 'GOOG','MSFT','FB','TSLA','DIS','EXPE','MRVL','BKNG','LUV','LHA.DE','JPM','HLT','H','NKE','MCD','JNJ','PFE']
stockdata=[]
def getData(symbol):
    headers = {'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.1 Safari/605.1.15'}
    url=f'https://uk.finance.yahoo.com/quote/{symbol}'
    r=requests.get(url, headers=headers)
    soup=BeautifulSoup(r.text, 'html.parser')
    stock={
        'symbol': symbol,
        'price': soup.find('div',{'class':'D(ib) Mend(20px)'}).find_all('span')[0].text,
        'change': soup.find('div',{'class':'D(ib) Mend(20px)'}).find_all('span')[1].text,
    }
    return stock

for item in mystocks:
    stockdata.append(getData(item))
    print('Getting: ', item)

with open('stockdata.json','w') as f:
    json.dump(stockdata, f)
print('Fin.')