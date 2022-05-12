
# liste = ["1","2","5a","10b","abc","10","50"]

# for i in liste:
#     try:
#         int(i)
#     except Exception as ex:
#         print(f"listenin {i} elemanı int değerine dönüştürülemiyor.\Hata türü: {ex}")
#     else:
#         print(f"listenin {i} elemanı int değerine dönüştürüldü.")

import re

# while True:
#     sayi = input("Sayı değeri giriniz: ")
#     if sayi == "q":
#         break
#     else:
#         try:
#             float(sayi)
#         except Exception as hata:
#             print("Sayı değeri girmediniz.\nHata türü: {}".format(hata))
#         else:
#             print("Geçerli giriş")
#             break


# def checkPassword(password):
#     if re.search("[çüöıÇÖÜİ1]",password):
#         raise Exception()


# parola = input("Parola Giriniz: ")

# try:
#     checkPassword(parola)
# except Exception as ex:
#     print("Şifre Türkçe karakter içermemelidir.")
# else:
#     print("geçerli şifre")

def factorial(x):
    if x > 0:
        toplam = 1
        while x > 1:
            toplam = x * toplam
            x -= 1
        print(toplam)
    elif x < 0:
        raise Exception()
    elif re.search("[A-B]",x):
        raise Exception()
    elif re.search("[a-b]",x):
        raise Exception()

x = int(input("faktöriyeli alınacak bir sayı giriniz:"))
try:
    factorial(x)
except:
    print("Yanlış bir sayı girdiniz.")
else:
    print("Geçerli sayı girdiniz.")

