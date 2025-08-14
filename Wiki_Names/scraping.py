import requests
from bs4 import BeautifulSoup
import json

url="https://tr.wiktionary.org/wiki/Kategori:T%C3%BCrk%C3%A7e_k%C4%B1z_adlar%C4%B1"

all_names=[]

while url:

    response=requests.get(url)
    response.encoding="utf-8" #türkçe karakterler düzgün gelsin
    soup=BeautifulSoup(response.text,"html.parser") # pc nin anlayacağı dil

    for tag in soup.select("div.mw-category-group li a"):
        all_names.append({"title":tag.text})
        #bulunan sayfadaki bütün isimleri alır


    next_link=None
    #sonraki sayfa butonu arar
    for a in soup.select("a"):
        if "sonraki sayfa" in a.text.lower():
            next_link="https://tr.wiktionary.org"+a["href"]
            break
    
    url=next_link

with open("woman_names_bs.json","w",encoding="utf-8")as f:
    json.dump(all_names,f,ensure_ascii=False,indent=4)

print(f"Toplam{len(all_names)} isim kaydedildi.")
