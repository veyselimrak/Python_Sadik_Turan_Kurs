
from select import select
from typing_extensions import Self


class Ucus():
    havayolu = "THY"

    def __init__(self, kod, kalkis, varis, sure, kapasite, yolcu):
        
        self.kod = kod
        self.kalkis = kalkis
        self.varis = varis
        self.sure = sure
        self.kapasite = kapasite
        self.yolcu = yolcu

    def anons_yap(self):
        
        return f"{self.kod} kodlu  {self.kalkis} - {self.varis} arası uçuşumuz  {self.sure} dakikada sürecektir."


    def kapasite_guncelleme(self):
        return self.kapasite - self.yolcu
    

    def __repr__(self):
        return f"{self.kod} kodlu seferimiz sisteme kayıt edilmiştir."
    

    def bilet_satis(self, bilet_adedi = 1):
    
        if self.yolcu + bilet_adedi <= self.kapasite:

            
            self.bilet_adedi = bilet_adedi
            self.yolcu += bilet_adedi
            print( f"{self.bilet_adedi} adet bilet satıldı. Kalan koltuk sayısı : {self.kapasite_guncelleme()} ")
    
        else:
            print("İşlem gerçekleştirilemedi. Yetersiz koltuk sayısı")

    def bilet_iptal(self, bilet_adedi=1):
        self.bilet_adedi = bilet_adedi
        if self.yolcu >= bilet_adedi:
            self.yolcu -= self.bilet_adedi
            print(f"{self.bilet_adedi} kadar biletiniz iptal edilmiştir. Kalan Koltuk sayısı :{self.kapasite_guncelleme()} ")

        else:
            print("İşlem gerçekleştirilemedi. Bilet Adedi kadar koltuk bulunamamaktadır.")

        

ucus2 = Ucus("TK123","İstanbul", "Ankara", 45, 300, 200)
ucus3 = Ucus("TK205", "Bodrum", "Siirt", 70, 250, 160)




# print(ucus2.kalkis)
# print(ucus2.havayolu)
# print(ucus3.anons_yap())
# print(ucus3.kapasite_guncelleme())
# print(ucus3.bilet_satis(50))
# print(ucus3.bilet_iptal(2))
# print(ucus3.bilet_iptal(300)) 

# Classın default olarak hangi metotlara sahip olduğunu gösterir. 
# print(ucus3.__dir__())

# print(ucus3)
## __repr__   sınıfın tutulduğu yerin adresi yerine gösterilecek yazı gösterilir.


class Seyahat():
    def __init__(self, kalkis, varis):
        self.kalkis = kalkis
        self.varis = varis


    def anons(self):
        return f"{self.kalkis} - {self.varis} seferimiz kalkışa hazır."
    
class Otobus(Seyahat):
    def __init__(self, kalkis, varis, mola_duraklari):
        super().__init__(kalkis, varis)
        self.mola_duraklari = mola_duraklari



seyahat1 = Seyahat("İstanbul", "Ankara")

print(seyahat1.anons())
        
otobus1 = Otobus("İstanbul", "Siirt", "Antalya , İzmir , Adana")

print(otobus1.anons())


