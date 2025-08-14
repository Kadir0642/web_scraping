import requests
from bs4 import BeautifulSoup
import json

url="https://tr.wikipedia.org/wiki/T%C3%BCrk_tarihi_kronolojisi#12._y%C3%BCzy%C4%B1l"

historical_events=[]

response=requests.get(url)
response.encoding="utf-8"

soup=BeautifulSoup(response.text,"html.parser")

for tag in soup.select("li"):
    date_tag=tag.find("b")
    if not date_tag:
        continue
    
    date=date_tag.get_text(strip=True)

    event_text=tag.get_text(" ",strip=True) #etiketleri birleştirirken aralara boşluk koyarak birleştirir
    event=event_text.replace(date,"",1).strip(" :")
    
    info={
        "date":date,
        "event":event
    }
    historical_events.append(info)

with open("historical_events.json","w",encoding="utf-8") as f:
    json.dump(historical_events,f,ensure_ascii=False,indent=4)

print(f"Toplam{len(historical_events)} olay kaydedildi")
