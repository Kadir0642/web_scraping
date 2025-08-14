from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import json

options=webdriver.ChromeOptions()
options.add_argument("--start-maximized")
driver=webdriver.Chrome(options)

driver.get("https://www.turkbitig.com/isimler/kiz.html")
time.sleep(2)

xpath="//a[contains(text(),'AÇELYA')]"
element=driver.find_element(By.XPATH,xpath)
link=element.get_attribute("href")
driver.get(link)
time.sleep(1)

male_data=[]

while True:
    
    xpath="//div[@class='content100']//b"
    name=driver.find_element(By.XPATH,xpath).text
    
    writing=driver.find_element(By.ID,"isim").text

    
    info={
        "title":name,
        "spelling":writing
    }
    male_data.append(info) # gelen veriyi kaydediyoruz

    if name=="ZEYNEP":
        print("tüm sayfalar tarandi")
        break
    else:
        xpath="//div[@id='prevnext']//a"
        button=driver.find_elements(By.XPATH,xpath)
    
        link=button[1].get_attribute("href") # 2. her zaman sonraki sayfa linkini veriyor
        driver.get(link)
        


driver.quit()
print("Veri sayisi:",len(male_data))

with open("woman.json","w",encoding="utf-8") as f:
    json.dump(male_data,f,indent=4, ensure_ascii=False)

print("Veriler 'woman.json' dosyasina kaydedilmistir")
