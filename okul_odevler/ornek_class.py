
class Calisan():

    personeller = []
    maaslar = []
    
    def __init__(self, ad, soyad, maas, butce):

        self.calisanAdi= ad
        self.calisanSoyadi = soyad
        self.calisanMaas = maas
        self.sirketButce = butce
    
    def calisanekleme(self):   
        self.personeller.append(self.calisanAdi)
        print(f" {self.calisanAdi} isimli çalışan sisteme kaydedildi. ")

    def maasekleme(self):
        self.maaslar.append(self.calisanMaas)
        print(f" {self.calisanAdi} isimli çalışanın maaşı sisteme kaydedildi. ")

    
    def calisanSilme(self):
        ad = input("Silinecek Ad: ")
        if ad in self.personeller:
            index = self.personeller.index(ad)
            del self.personeller[index]
        print(f" {self.calisanAdi} isimli çalışan sisteme kaydedildi. ")

    def toplamMaas(self):
        self.maaslar.append(self.calisanMaas)
        print(self.maaslar)

    def sirketButce(self):
        print(f"Şirket Bütçesi: {self.sirketButce}")

    def butceEkleme(self):
        butce = float(input("Eklenecek Bütçe Fiyatını Giriniz: "))
        self.sirketButce += butce
        print(f"Yeni Bütçeniz Toplam: {self.sirketButce}")

    def butceSilme(self):
        butce = float(input("Silinecek bütçeyi giriniz: "))
        self.sirketButce -= butce
        print(f"Yeni Bütçeniz Toplam: {self.sirketButce}")

calisan1 = Calisan("selim", "inanır", 5000, 45000)

calisan1.butceEkleme()
calisan1.calisanekleme()
calisan1.butceSilme()
