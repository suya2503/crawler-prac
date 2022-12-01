import requests
from bs4 import BeautifulSoup
import pandas as pd

r = requests.get("https://chart.capital.com.tw/Chart/TWII/TAIEX11.aspx")

if r.status_code == requests.codes.ok:
    print("It's ok to be parsed.")
    soup = BeautifulSoup(r.text, "lxml") # 另一個常用的parser:lxml為了速度上的追求
    s_tables = soup.find_all("table", attrs={"cellpadding":"2"})

    table_data = []
    for table in s_tables:
        table_columns = []
        trs = table.find_all("tr")
        for tr in trs:
            row = [td.text for td in tr.find_all("td")]
            if row[0] == "日期":
                table_columns = row
                continue
            table_data.append(row)
    
    df = pd.DataFrame(data = table_data, columns=table_columns)
    

    df.to_csv("./data/big_eight.csv", mode="w", index=False)
    df.to_html("./data/big_eight.html", index=False)
