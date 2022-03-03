from traceback import print_tb
from unicodedata import name


ogrenciler = {}

number = input("Ogrenic Numaranızı Giriniz : ")
name = input("Adınızı Giriniz : ")
lastName = input("Soyadınızı Giriniz :")
phoneNumber = input("Telefon Numaranızı Giriniz :")

ogrenciler.update(
    {
         number  : {
             "Adı" : name,
             "Soyadı" :lastName,
            "Telefon Numarası" : phoneNumber
        }
    }
)
number = input("Ogrenic Numaranızı Giriniz : ")
name = input("Adınızı Giriniz : ")
lastName = input("Soyadınızı Giriniz :")
phoneNumber = input("Telefon Numaranızı Giriniz :")

ogrenciler.update(
    {
         number  : {
             "Adı" : name,
             "Soyadı" :lastName,
            "Telefon Numarası" : phoneNumber
        }
    }
)

number = input("Ogrenic Numaranızı Giriniz : ")
name = input("Adınızı Giriniz : ")
lastName = input("Soyadınızı Giriniz :")
phoneNumber = input("Telefon Numaranızı Giriniz :")

ogrenciler.update(
    {
         number  : {
             "Adı" : name,
             "Soyadı" :lastName,
            "Telefon Numarası" : phoneNumber
        }
    }
)

print(ogrenciler)


veriAlma = input("Bilgisini görmek istediğiniz öğrencinin numarasını giriniz :  ")

print(ogrenciler[veriAlma])

