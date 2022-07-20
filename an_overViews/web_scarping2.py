
import requests
from bs4 import BeautifulSoup

url ="https://www.n11.com/bilgisayar/dizustu-bilgisayar"

html = requests.get(url).content

soup = BeautifulSoup(html,"html.parser")

soup.prettify()

list = soup.find_all("li",{"class":"column"})

for link in list:
    name = link.h3.string
    price = link.find("del").string
    star = link.find("span",{"class":"ratingText"}).string.strip("()")
    print(f" Ürün Adı: {name.ljust(108)}  Fiyatı: {price}  Reytingi: {star}  ")