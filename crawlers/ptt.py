import requests
from bs4 import BeautifulSoup
import os

ROOT_URL = 'https://disp.cc/b'
r = requests.get(os.path.join(ROOT_URL, "PttHot")) # sent 要求

soup = BeautifulSoup(r.text, 'html.parser')

# 使用最常見的功能來擷取某些tag的內容 -> 觀察網頁原始碼的HTML組成

span_tag_list = soup.find_all("span", class_="L34 nowrap listTitle") # 取得tag為span, 且class為L34 nowrap listTitle

titles = [span.text for span in span_tag_list] # 因為這個span僅有一個text所以可以不用再往下一層tag找尋 
print(titles)

# tag a的屬性有href, 可以用get或是字典索引方式取得
titles_info = {span.text:os.path.join(ROOT_URL, span.find("a").get("href")) for span in span_tag_list if span.text != "□ [公告] PTT 熱門文章板 開板成功"}
print(titles_info)


titles_info = {}
for span in soup.select("span.listTitle.L34.nowrap"):
    if span.text != "□ [公告] PTT 熱門文章板 開板成功":
        titles_info.update({span.text:os.path.join(ROOT_URL, span.find("a").get("href"))})

print(titles_info)
