import requests
import json

class imdb:

    def __init__(self):

        self.api_url = "https://imdb-api.com/en/API"
        self.api_key = "k_2asjwir2"

    def get_populer_films (self):
        response = requests.get(self.api_url + "/MostPopularMovies/" + self.api_key)
        return response.json()

    def get_BoxOffice (self):
        response = requests.get(self.api_url + "/BoxOffice/" + self.api_key)
        return response.json()

    def search_film (self, nameoffilm):
        response = requests.get(self.api_url + "/SearchMovie/" + self.api_key + "/" + nameoffilm)
        return response.json()
    
    def search_series (self, nameofseries):
        response = requests.get(self.api_url + "/SearchSeries/" + self.api_key + "/" + nameofseries)
        return response.json()
    
user1 = imdb()

while True:
    
    secim = input("1-Populer Films\n2- Trailers\n3- Search Film\n4- Search Series\n5-Exit\nSeçiminiz: ")

    if secim == "5":
        break
    else:
        if secim == "1":
            movies = user1.get_populer_films()
            for movie in movies['items']:
                print(movie['title'])           

        elif secim == "2":
            movies = user1.get_BoxOffice()
            for movie in movies['items']:
                print(movie['title'])  

        elif secim == "3":
            name_film = input("Film İsmi Giriniz: ")
            result = user1.search_film(name_film)
            print(result)

        elif secim == "4":
            name_film = input("Film İsmi Giriniz: ")
            result = user1.search_film(name_film)
            print(result)

        else:
            print("Yanlış Seçim Yaptınız.")