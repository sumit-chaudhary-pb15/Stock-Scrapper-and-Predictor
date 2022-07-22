import json
import pprint
import requests
from bs4 import BeautifulSoup
from constants import headers


def get_stock_data(symbol):
    url = f'https://finance.yahoo.com/quote/{symbol}'
    r = requests.get(url, headers=headers, timeout=5)
    # print(r.status_code)
    # print(r.text)
    soup = BeautifulSoup(r.text, 'html.parser')
    # print(soup.title.text)
    # print(symbol)
    # print(soup.find('div', {'class': 'D(ib) Mend(20px)'}))
    stock_data = dict(
        price=soup.find('div', {'class': 'D(ib) Mend(20px)'}).find_all('fin-streamer')[0].text,
        change=soup.find('div', {'class': 'D(ib) Mend(20px)'}).find_all('fin-streamer')[1].text,
        change_percent=soup.find('div', {'class': 'D(ib) Mend(20px)'}).find_all('fin-streamer')[2].text,
        close_price=soup.find('div', {'class': 'D(ib) W(1/2) Bxz(bb) Pend(12px) Va(t) ie-7_D(i) smartphone_D(b) smartphone_W(100%) smartphone_Pend(0px) smartphone_BdY smartphone_Bdc($seperatorColor)'}).find_all('td')[1].text,
        open_price=soup.find('div', {'class': 'D(ib) W(1/2) Bxz(bb) Pend(12px) Va(t) ie-7_D(i) smartphone_D(b) smartphone_W(100%) smartphone_Pend(0px) smartphone_BdY smartphone_Bdc($seperatorColor)'}).find_all('td')[3].text,
        range_price=soup.find('div', {'class': 'D(ib) W(1/2) Bxz(bb) Pend(12px) Va(t) ie-7_D(i) smartphone_D(b) smartphone_W(100%) smartphone_Pend(0px) smartphone_BdY smartphone_Bdc($seperatorColor)'}).find_all('td')[9].text,
        volume=soup.find('div', {'class': 'D(ib) W(1/2) Bxz(bb) Pend(12px) Va(t) ie-7_D(i) smartphone_D(b) smartphone_W(100%) smartphone_Pend(0px) smartphone_BdY smartphone_Bdc($seperatorColor)'}).find_all('td')[13].text
    )
    return stock_data


my_stocks = ['GOOG', 'CANBK.BO']
stock_data = []

for stock in my_stocks:
    data = get_stock_data(stock)
    data.update({'stock': stock})
    stock_data.append(data)

pp = pprint.PrettyPrinter(indent=2, width=30, compact=True)
pp.pprint(stock_data)

with open('stockdata.json', 'w') as f:
    json.dump(stock_data, f)
