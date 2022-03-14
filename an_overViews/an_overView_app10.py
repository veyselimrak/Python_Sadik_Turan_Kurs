from typing import OrderedDict, final

number = float(input("Bir Sayı Giriniz :"))

if number > 0 and number < 100:
    print("Sayı 0 ile 100 arasındadır.")
else:
    print("Sayı 0 ile 100 arasında değildir.") 

if number > 0:
    if number % 2 == 0:
        print("Sayı Pozitif çift sayıdır.")
    else:
        print("Sayı Pozitif ama Çift değildir.")
else:
    print("Sayı Pozitif Değildir.")

email = input("Email adresinizi giriniz :")
password = input("Şifrenizi Giriniz :")

if email == "veyselimrak66@gmail.com":
    if password == "abc123":
        print("Email Ve Şifreniz doğrulandı.")
    else:
        print("Emailiniz doğru ama şifreniz yanlış tekrar deneyiniz...")
else:
    print("Email adresiniz yanlış tekrar deneyiniz...")

number1 = float(input("1.Sayıyı Giriniz :"))
number2 = float(input("2.Sayıyı Giriniz :"))
number3 = float(input("3.Sayıyı Giriniz :"))

if number1 > number2 and number1 > number3:
    if number2 > number3:
        print(f"1. Sayı {number1} > 2.Sayı {number2} > 3.Sayı{number3}")
    else:

        print(f"1. Sayı {number1} > 3.Sayı{number3} > 2.Sayı {number2}")

elif number2 > number1 and number2 > number3:
    if number1 > number3:
        print(f"2.Sayı {number2} > 1. Sayı {number1} > 3.Sayı{number3}")
    else:
        print(f"2.Sayı {number2} > 3.Sayı {number3} > {number1}")
elif number3 > number1 and number3 > number2:
    if number1 > number2:
        print(f"3.Sayı {number3} > 1. Sayı {number1} > 2.Sayı {number2}")
    else:
        print(f"3.Sayı {number3} > 2.Sayı {number2} > 1. Sayı {number1}")

from typing import OrderedDict, final


vize1 = float(input("1.Vize Notunuzu  Giriniz :"))
vize2 = float(input("2.Vize Notunuzu  Giriniz :"))
final = float(input("Final Notunuzu  Giriniz :"))

ort =  ( (vize1  + vize2 ) * 0.4 ) + final * 0.6

print(ort)

if ort > 49 and ort < 101 and final > 50:
    print("Geçti")
elif final > 70 and final < 101:
    print("Geçti.")
elif ort > 0 and ort < 50:
    print("Kaldı.")
else:
    print("Notlar Yanlış girildi. Tekrar deneyiniz...")

name = input("Adınızı Giriniz :")
size = float(input("Boyunuzun uzunluğunu metre cinsinden Giriniz :"))
weight = float(input("Kilonuzu Giriniz :"))

endeks = (weight / (size ** 2))

if endeks > 0 and endeks < 18.5:
    print("Zayıf")
elif endeks > 18.4 and endeks < 25.0:
    print("Normal")
elif endeks > 25.1 and endeks < 30.0:
    print("Kilolu")
elif endeks > 30.1 and endeks < 35.0:
    print("Obezite")
else:
    print("Yanlış Giriş Yaptınız. Tekrar Deneyiniz...")
