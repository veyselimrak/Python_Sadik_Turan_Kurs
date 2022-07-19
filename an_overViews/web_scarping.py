from turtle import title
import requests
from bs4 import BeautifulSoup

url = "https://www.imdb.com/chart/moviemeter/?ref_=nv_mv_mpm"

html = requests.get(url).content

soup = BeautifulSoup(html, "html.parser")

list = soup.find("tbody",{"class":"lister-list"}).find_all("tr",limit=10)


count = 0
for tr in list:
    title = tr.find("td",{"class":"titleColumn"}).a.string
    year = tr.find("td",{"class":"titleColumn"}).find("span",{"class":"secondaryInfo"}).string.strip("()")
    imdb_puan = tr.find("td",{"class":"ratingColumn imdbRating"}).strong.string
    count += 1
    print(f" {count}.film: {title.ljust(45)} yıl: {year} imdb puanı: {imdb_puan}   ")


