
from typing_extensions import Self

from sympy import true


class HesapMakinesi:
    def __init__(self, secim, uzunluk, taban, yukseklik):
        self.secim = secim
        self.uzunluk = uzunluk
        self.taban = taban
        self.yukseklik = yukseklik

        self.anaMenu(self)
    
    def anaMenu(self, secim):
        if self.secim == "1":
            sonuc = self.kareAlan()
            self.ekranaYaz(sonuc)
        elif secim == "quit":
            quit()
        elif self.secim == "2":
            sonuc = self.kareCevre()
            self.ekranaYaz(sonuc)
        elif  secim == "3":
            sonuc = self.dikdortgenAlan()
            self.ekranaYaz(sonuc)
        elif secim == "4":
            sonuc = self.dikdortgenCevre()
            self.ekranaYaz(sonuc)
    def kareAlan(self):
        return self.uzunluk * self.uzunluk
    def kareCevre(self):
        return self.uzunluk * 4
    def dikdortgenAlan(self):
        return self.taban * self.uzunluk
    def dikdortgenCevre(self):
        return (self.taban * 2 ) + (self.uzunluk * 2)
    def ekranaYaz(self, sonuc):
        print(sonuc)

while True:
    print("""
    1:kare alan
    2:kare çevre
    3:dikdörtgen alan
    4:dikdörtgen çevre
    çıkış için quit yazınız.
    """)

    secim = input("1-4 arası sayı seçiniz: ")
    uzunluk = float(input("uzunluk giriniz: "))
    taban = float(input("Taban uzunluğu giriniz: "))
    yukseklik = float(input("Yükseklik giriniz: "))

    hesap = HesapMakinesi(secim,uzunluk,taban,yukseklik)
