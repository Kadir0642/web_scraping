import requests
from bs4 import BeautifulSoup
import json

url = "https://www.tdpb.org.tr/post/ge%C3%A7mi%CC%87%C5%9Ften-g%C3%BCn%C3%BCm%C3%BCze-t%C3%BCrk-devletleri%CC%87"

response = requests.get(url)
response.encoding = "utf-8"
soup = BeautifulSoup(response.text, "html.parser")

countries = []
# Tüm content metin bloklarını listeliyoruz
# Başlık satırı genelde <p> veya doğrudan içerikte. Burada h4/h5 yok, düz metin.
# Biz başlık satırlarını büyük harf ve ' - ' içeriklerine göre seçiyoruz.
for element in soup.select("body")[0].find_all(text=True):
    txt = element.strip()
    if not txt:
        continue
    # Başlangıç kısmında büyük harfle ve '-' içeriyorsa
    if " - " in txt and txt.upper() == txt:
        # Bu bir başlık satırı olabilir
        try:
            title, period = txt.split(" - ", 1)
        except ValueError:
            title = txt
            period = ""
        # Sonraki kardeş içerik açıklama olabilir
        next_txt = element.find_next(string=True)
        description = next_txt.strip() if next_txt else ""
        countries.append({
            "title": title.strip(),
            "period": period.strip(),
            "description": description
        })

with open("countries.json", "w", encoding="utf-8") as f:
    json.dump(countries, f, ensure_ascii=False, indent=4)
