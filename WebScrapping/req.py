from bs4 import BeautifulSoup
import requests as rs
import pandas as pd
html_get= rs.get("https://www.airbnb.co.in/s/United-States/homes?adults=2&place_id=ChIJCzYy5IS16lQRQrfeQ5K5Oxw").text
soup=BeautifulSoup(html_get,'lxml')
cont=soup.find_all('div',class_="t1jojoys dir dir-ltr")
name=[]
rating=[]
price=[]
for i in cont:
    name.append(i.text)
cont=soup.find_all('span',class_="_tyxjp1")
for i in cont:
    price.append(i.text)
cont=soup.find_all('span',class_='t5eq1io r4a59j5 dir dir-ltr')    
for i in cont:
    rating.append(i.text)
print(name)
print(price)
print(rating)

dict = {"Name": name, "Price": price,
        "Rating": rating}
df = pd.DataFrame(dict)
df.to_csv('data.csv')
