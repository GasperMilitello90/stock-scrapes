import requests
from bs4 import BeautifulSoup
import datetime
import sqlite3

conn = sqlite3.connect('techstockdata.db')
c = conn.cursor()

#c.execute('''CREATE TABLE techstocks(date DATE, stock TEXT, price REAL, pricechange REAL, pctchange TEXT)''' )
def getStockdataNVDA(url):
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36'}
    r = requests.get(url, headers=headers)
    soup = BeautifulSoup(r.content, 'html.parser')
    current_date = datetime.datetime.now()
    stock = 'NVDA'
    price = soup.find('div', {'class': "D(ib) Mend(20px)"}).find_all('fin-streamer')[0].text
    pricechange = soup.find('div', {'class': "D(ib) Mend(20px)"}).find_all('fin-streamer')[1].text
    pctchange = soup.find('div', {'class': "D(ib) Mend(20px)"}).find_all('fin-streamer')[2].text
    c.execute('''INSERT INTO techstocks VALUES (?, ?, ?, ?, ?)''', (current_date, stock, price, pricechange, pctchange))
    #print(current_date, stock, price, pricechange, pctchange)
    return

def getStockdataAMD(url):
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36'}
    r = requests.get(url, headers=headers)
    soup = BeautifulSoup(r.content, 'html.parser')
    current_date = datetime.datetime.now()
    stock = 'AMD'
    price = soup.find('div', {'class': "D(ib) Mend(20px)"}).find_all('fin-streamer')[0].text
    pricechange = soup.find('div', {'class': "D(ib) Mend(20px)"}).find_all('fin-streamer')[1].text
    pctchange = soup.find('div', {'class': "D(ib) Mend(20px)"}).find_all('fin-streamer')[2].text
    c.execute('''INSERT INTO techstocks VALUES (?, ?, ?, ?, ?)''', (current_date, stock, price, pricechange, pctchange))
    #print(current_date, stock, price, pricechange, pctchange)
    return

def getStockdataAMZN(url):
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36'}
    r = requests.get(url, headers=headers)
    soup = BeautifulSoup(r.content, 'html.parser')
    current_date = datetime.datetime.now()
    stock = 'AMZN'
    price = soup.find('div', {'class': "D(ib) Mend(20px)"}).find_all('fin-streamer')[0].text
    pricechange = soup.find('div', {'class': "D(ib) Mend(20px)"}).find_all('fin-streamer')[1].text
    pctchange = soup.find('div', {'class': "D(ib) Mend(20px)"}).find_all('fin-streamer')[2].text
    c.execute('''INSERT INTO techstocks VALUES (?, ?, ?, ?, ?)''', (current_date, stock, price, pricechange, pctchange))
    #print(current_date, stock, price, pricechange, pctchange)
    return

def getStockdataTSLA(url):
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36'}
    r = requests.get(url, headers=headers)
    soup = BeautifulSoup(r.content, 'html.parser')
    current_date = datetime.datetime.now()
    stock = 'TSLA'
    price = soup.find('div', {'class': "D(ib) Mend(20px)"}).find_all('fin-streamer')[0].text
    pricechange = soup.find('div', {'class': "D(ib) Mend(20px)"}).find_all('fin-streamer')[1].text
    pctchange = soup.find('div', {'class': "D(ib) Mend(20px)"}).find_all('fin-streamer')[2].text
    c.execute('''INSERT INTO techstocks VALUES (?, ?, ?, ?, ?)''', (current_date, stock, price, pricechange, pctchange))
    #print(current_date, stock, price, pricechange, pctchange)
    return

def getStockdataMSFT(url):
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36'}
    r = requests.get(url, headers=headers)
    soup = BeautifulSoup(r.content, 'html.parser')
    current_date = datetime.datetime.now()
    stock = 'MSFT'
    price = soup.find('div', {'class': "D(ib) Mend(20px)"}).find_all('fin-streamer')[0].text
    pricechange = soup.find('div', {'class': "D(ib) Mend(20px)"}).find_all('fin-streamer')[1].text
    pctchange = soup.find('div', {'class': "D(ib) Mend(20px)"}).find_all('fin-streamer')[2].text
    c.execute('''INSERT INTO techstocks VALUES (?, ?, ?, ?, ?)''', (current_date, stock, price, pricechange, pctchange))
    #print(current_date, stock, price, pricechange, pctchange)
    return


getStockdataNVDA('https://finance.yahoo.com/quote/NVDA')
getStockdataAMD('https://finance.yahoo.com/quote/AMD')
getStockdataAMZN('https://finance.yahoo.com/quote/AMZN')
getStockdataTSLA('https://finance.yahoo.com/quote/TSLA')
getStockdataMSFT('https://finance.yahoo.com/quote/MSFT')

conn.commit()
print('complete.')

c.execute('''SELECT * FROM techstocks''')
results = c.fetchall()
print(results)

conn.close()