import requests
from bs4 import BeautifulSoup

r = requests.get("https://tw.stock.yahoo.com/quote/2330")

if r.status_code == requests.codes.ok:
    # 先將網頁給解析成html
    soup = BeautifulSoup(r.text, "html.parser")

    # 在針對要爬的地方選取獨特性 
    # 找html架構時，最好找具有獨特性的tag
    # 若沒有獨特性 -> 順序：找出這個tag:table的是在哪一個順序
    table = soup.find_all('table')[2]
    print(table)

    price = table.find_all('td')[2]
    buy_price = price.find_next('td')
    sell_price = buy_price.find_next('td')
    print(f"price:{price.text}, buy_price:{buy_price}, sell_price:{sell_price}")