import random

rastgele_sayi = random.randint(0,100)

#BENİM YAPTIĞIM :
# hak = int(input("Kaç Hakta bulabileceksiniz :"))
# puan = 100
# for tahmin in range(hak):
#     tahmininiz = int(input("0-100 Arası Tahmininizi Giriniz : "))
#     if rastgele_sayi ==  tahmininiz:
#         print("Tebrikler Oyunu Kazandınız.")
#         print(f"Oyun Puanınız : {puan} ")
#         break
#     elif rastgele_sayi > tahmininiz:
#         print("Yukarı Çık")
#         puan = puan - 10
#     elif rastgele_sayi < tahmininiz:
#         print("Aşağı İn")
#         puan = puan - 10
#     else:
#         print("Yanlış Bir Sayı Girdiniz.")

#HOCANIN YAPTIĞI : 
hak = 10
puan = 100
while hak > 0:
    tahminim = int(input("Tahmin : "))
    if hak == 0:
        print("Hakkınız Bitti ")
    if rastgele_sayi == tahminim:
        print("Tebrikler Sayıyı Tahmin Ettiniz. \n Oyun Puanınız : {}".format(puan))
        break
    elif rastgele_sayi < tahminim:
        print("Aşağı")
        puan -= 10
    elif rastgele_sayi > tahminim:
        print("Yukarı")
        puan -= 10
    else:
        print("Yanlış Sayı Girdiniz.")
    hak -= 1
    print("Kalan Hak : {}".format(hak))
    
