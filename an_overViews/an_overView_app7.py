
from typing import final
from unittest import result


a = int(input("1. Sayıyı Giriniz :"))
b = int(input("2. Sayıyı Giriniz :"))

print(a>b)

vize1 = float(input("Vize 1 : "))
vize2 = float(input("Vize 2 : "))
final = float(input("Final : "))

ort = ((vize2 + vize1) / 2) * 0.6 + (final * 0.4)

print(f"Ortalamanız : {ort} Dersten geçme durumunuz : {ort>=50}")

x = int(input("Sayıyı Giriniz :"))
tekcift = (x % 2 == 0)
print(f"{x} sayısı çift mi :  {tekcift} ")

y = int(input("Sayıyı Giriniz :"))
pozitifnegatif = y > 0
print(f"{y} sayısının pozitif negatif olma durumu : {pozitifnegatif}")

password = input("Parolanızı Giriniz : ")
userName = input("Kullanıcı Adınızı Giriniz :")

print(password == "abc123" )
print(userName == "email@sadikturan.com")








