
a = 1
b = 1
c = 0
n = [a,b,c]
sayi = int(input("Sayı giriniz : "))

if sayi == 1 or sayi == 2:
    print("{}. terimin değeri : {} ".format(sayi,n[0]))
elif sayi > 2 :
    for x in range(2,sayi):
        n[x] = n[x-1] + n[x-2]
        n.append(n[x])

    print("{}. terimin değeri : {} ".format(sayi,n[x]))

import string

o_karakterler = string.punctuation
b_harfler = string.ascii_uppercase
k_harfler = string.ascii_lowercase
t_karakterler = "çğıöşüIÇĞÖÜ"

kontrol = False
while not kontrol:
    k_adi = input("Kullanıcı adı giriniz : ")
    if len(k_adi) == 0:
        print("Kullanıcı adı boş geçilemez.")
    elif len(k_adi) > 20:
        print("Karakter sayısı max 20 olmalıdır.")
    else:
        a = 0
        for o_karakter in o_karakterler:
            if o_karakter in k_adi:
                print("Kullanıcı adı özel karakter içermemelidir.")
                break
            else:
                a += 1
        b = 0
        for t_karaker in t_karakterler:
            if t_karaker in k_adi:
                print("Kullanıcı adı türkçe karakter içermemeli")
                break
            else:
                b += 1
        if a == 0 and b == 0:
            print("Tekrar deneyin.")
        elif a > 0 and b > 0:
            print("Kullanıcı adınız başarıyla kaydedildi.\nŞifreye gidin.")
            kontrol = True
            

kontrol = False
while not kontrol:
    parola = input("Şifrenizi Giriniz :")
    a = 0
    for o_karakter in o_karakterler:
            if o_karakter in parola:
                print("Kullanıcı adı özel karakter içermemelidir.")
                a += 1
    b = 0
    for b_harf in b_harfler:
            if b_harf in parola:
                print("Kullanıcı adı özel karakter içermemelidir.")
                b += 1        
    c = 0
    for k_harf in k_harfler:
            if k_harf in parola:
                print("Kullanıcı adı özel karakter içermemelidir.")
                c += 1
    print("Şifreniz başarıyla kaydedildi.")
    

    if a == 0 and b == 0 and c > 0:
        print("Şifre kötü")
    elif a > 0 and b > 0:
        print("Şifre orta")
        kontrol  =True
    elif a > 0 and b > 0 and c > 0:
        print("Şifre zor")
        kontrol = True

secim = input("Giriş : p Çıkış : q basın")

if secim == "p":
    print("Sisteme başarıyla giriş yapıldı. Yönlendiriliyorsunuz.")
elif secim == "q":
    print("Sistemden çıkılıyor.")
    quit()
elif secim != "p" and secim != "q":
    print("Yanlış seçim yapıldı.")
        

