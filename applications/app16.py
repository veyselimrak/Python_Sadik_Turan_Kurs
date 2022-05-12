

# print(a) => NameError
# int("1a2") => ValueError
# print(10/0) => ZeroDivisionError
# print("denem"e) => SyntaxError


#error handling => hata yönetimi

try:
    x = int(input("X : "))
    y = int(input("Y : "))
    print(x/y)
except Exception as hata:
    print(f"Yanlış Bilgi Girdiniz.\nHata türünüz: {hata}")
else:
    print("İşlem Tamamlandı.")
finally:
    print("Tur Tamamlandı.")


def checkPassword(password):
    import re
    if len(password) > 10:
        raise Exception("Şifre 10 karakterden küçük olmalıdır.")
    elif not re.search("[a-z]", password):
        raise Exception("Şifrede küçük harf bulunmalıdır.")
    elif not re.search("[A-Z]", password):
        raise Exception("Şifrede büyük harf olmalıdr.")
    elif not re.search("[0-9]", password):
        raise Exception("Şifrede rakam olmalıdır.")
    elif re.search("\s", password):
        raise Exception("Şifrede boşluk bulunmamalıdır.")
    else:
        print("Geçerli parola")



psw = input("Şifrenizi oluşturunuz: ")

try:
    checkPassword(psw)
except Exception as ex:
    print("Yanlış bilgi girdiniz.\nHata türünüz : {}".format(ex))
else:
    print("Şifreniz tamamlandı.")




    
