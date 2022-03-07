from unicodedata import name
import datetime
from datetime import date
# 1.Soru
# name = input("Adınızı Giriniz :")
# age = int(input("Yaşınızı Giriniz : "))
# schoolinfo = input("Eğitim Bilgilerinizi Giriniz :")

# if age > 18: 
#     if  schoolinfo == "lise" or schoolinfo =="üniversite"  :
#         print("Ehliyet alabilir .")
#     else:
#         print("Ehliyet alamaz .")
# else:
#     print("Ehliiyet alamaz.")

# 2.Soru
# yazili1 = float(input("Yazılı 1 :"))
# yazili2 = float(input("Yazılı 2 :"))
# sozlu = float(input("Sözlü :"))

# ort = (yazili2 + yazili1 + sozlu) / 3

# if 0 < ort <= 25:
#     print("Ortalamanız : 0 ")
# elif 25 < ort <=44:
#     print("Ortalamanız : 1")
# elif 44 < ort <= 54:
#     print("Ortalamanız : 2")
# elif 54 < ort <= 69:
#     print("Ortalamanız : 3")
# elif 69 < ort <= 84:
#     print("Ortalamanız: 4")
# elif 84 < ort <= 100:
#     print("Ortalamanız : 5")
# else:
#     print("Notlarınızı Yanlış Girdiniz.\nLütfen Tekrar Deneyiniz.")


cikisYili = int(input("Çıkış Yılınız Giriniz : "))
cikisAyi = int(input("Çıkış Ayını giriniz : "))
cikisGunu= int(input("Çıkış Gününü giriniz :"))
cikisTarihi = date(cikisYili,cikisAyi,cikisGunu)

print(cikisYili)

bugun = date.today()

bakimTarihi = bugun - cikisTarihi
print(bakimTarihi)

if bakimTarihi.days > 365 :
    print("Aracınızın 1.Bakım Zamanı gelmiş.")
elif bakimTarihi.days > 365 * 2 :
    print("Aracınızın 2.Bakım Zamanı Gelmiş")
elif bakimTarihi.days > 365 * 3:
    print("Aracınızın 3.Bakım Tarihi Gelmiş")
else:
    print("Aracınızın Henüz Bakım Zamanı Gelmemiş")

