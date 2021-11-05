import requests
from bs4 import BeautifulSoup

URL = 'https://www.tinkoff.ru/invest/stocks/?country=All&orderType=Asc&sortType=ByName&start=0&end=12'
HEADERS = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36',
    'accept': '*/*'}


def get_HtmlSource(url, params=None):
    result = requests.get(url, headers=HEADERS, params=params)
    return result


def get_content(source):
    soup = BeautifulSoup(source.text, "html.parser")
    Stock = soup.find_all('a', {"href": '/invest/stocks/MMM/'})

    Stock_Price = 0
    Stock_Name = ""
    Stock_Currency = ""

    item = Stock[0]
    name = item.find('span', {"class": "NameColumn__nameWrapper_177eF"}).get_text()
    Name = name
    item = Stock[2]
    price = item.find(("span", {"class": "Money-module__money_3h4MT"})).get_text()
    Price = price

    print(Name)
    print(Price)


def parse():
    source = get_HtmlSource(URL)

    if source.status_code == 200:
        get_content(source)
    else:
        print("Request failed")


parse()