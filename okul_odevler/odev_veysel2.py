import string

secim = False
while not secim:

    k_adi =  input("Kullanıcı Adı : ")
    rakamlar = "0123456789"

    b_harfler = string.ascii_uppercase
    k_harfler = string.ascii_lowercase
    o_karakterler = string.punctuation
    
    if len(k_adi) <= 16:
            a = 0
            for rakam in k_adi:
                if rakam in rakamlar:
                    a += 1

            if a > 0:
                pass
            else:
                print("Kullanıcı adınıza rakam ekleyiniz.")
            b = 0
            for b_harf in k_adi:
                if b_harf in b_harfler:
                        b += 1
            if b > 0:
                pass
            else:
                print("Kullanıcı adınıza büyük harf ekleyiniz.")

            c = 0
            for k_harf in k_adi:
                if k_harf in k_harfler:
                        c += 1
            if c > 0:
                pass
            else:
                print("Kullanıcı adınıza küçük harf ekleyiniz.")
            d = 0
            for o_karakter in k_adi:
                if o_karakter in o_karakterler:
                        d += 1
            if d > 0:
                print("Kullanıcı adında özel karakter bulunmamalı. ")
                
            else:
                if a > 0 and b > 0 and c > 0 and d == 0:
                    print("Kullanıcı adınız başarıyla kaydedildi.")
                    secim = True
    else:
        print("Kullanıcı adı karakter uzunluğu 16dan küçük olmalıdır.")

secim = False
while not secim:

    password = input("Şifre : ")
    rakamlar = "0123456789"
    b_harfler = string.ascii_uppercase
    k_harfler = string.ascii_lowercase 
    o_karakterler = string.punctuation
    
    if len(password) >= 8 and len(password) <= 24:
            a = 0
            for rakam in password:
                if rakam in rakamlar:
                    a += 1

            if a > 0:
                pass
            else:
                print("Şifrenize rakam ekleyiniz.")
            b = 0
            for b_harf in password:
                if b_harf in b_harfler:
                        b += 1
            if b > 0:
                pass
            else:
                print("Şifrenize büyük harf ekleyiniz.")

            c = 0
            for k_harf in password:
                if k_harf in k_harfler:
                        c += 1
            if c > 0:
                pass
            else:
                print("Şifrenize küçük harf ekleyiniz.")
            d = 0
            for o_karakter in password:
                if o_karakter in o_karakterler:
                        d += 1
            if d > 0:
                if a > 0 and b > 0 and c > 0 and d > 0:
                    print("Şifreniz başarıyla kaydedildi.\n")
                    secim = True
                
            else:
                print("Şifrenizde özel karakter bulunmalı.")
                
    else:
        print("Şifre karakter uzunluğu 8'den büyük 24'den küçük olmalıdır.")

   
_k_adi = "Veysel12"
_password = "passWord12_"

def calculator():
    """-
    4 İşlem Hesap Makinesine Hoşgeldiniz... 
    """
    veri = input("İşleminizi yapınız. --> ")
    islem = eval(veri)
    print(islem)

if k_adi == _k_adi and password == _password:
    print("Hesaba başarıyla giriş yapıldı.\n") 
    print("Uy-gulamaya yönlendiriliyorsunuz.")
    calculator()
    
elif k_adi == _k_adi and password != _password:
    print("Şifrenizi yanlış girdiniz.\nLütfen tekrar deneyin.")

elif k_adi != _k_adi and password == _password:
    print("Böyle bir kullanıcı adı bulunmamaktadır.\nLütfen tekrar deneyin.")

elif k_adi != _k_adi and password != _password:
    print("Kullanıcı adı ve şifre yanlış!!!\nLütfen tekrar deneyin")     

else:
    print("Hesaba Giriş yapılamadı.")
