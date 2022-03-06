from cgi import print_form
from gettext import npgettext
from unicodedata import name
from unittest import result


number = int(input("Sayı Giriniz : "))

result = 0 < number < 100
print(result) 

result = number > 0 and number % 2 == 0

email = input("Email Giriniz : ")
password = input(("Şifrenizi Giriniz : "))


result = (email == "email@veyselimrak.com") and (password == "abc123")


vize1 = float(input("Vize 1 :"))
vize2 = float(input("Vize 2 :"))
final = float(input("Final : "))

result = ((vize1+vize2) / 2) * 0.6 + final * 0.4
gecmekalma = ( result > 50 and final > 50 ) or (final > 70)
result = print(f"Ortalmanız : {result}  Dersten geçme durumuz : {gecmekalma}")

name = input("Adınızı Giriniz: ")
size = float(input("Boyunuzu Giriniz : "))
weight = float(input("Kilonuzu Giriniz :"))

result = ( weight) / (size ** 2)

zayif = 0 <= result <= 18.4 
normal =  18.5 <= result <= 24.9 
kilolu = 25 <= result <= 29.9 
obez = 30.0 <= result <= 34.9 

print(f"{name} kilo indeksin : {result} ve kilo değerlendirmen {zayif}")
print(f"{name} kilo indeksin : {result} ve kilo değerlendirmen {normal}")
print(f"{name} kilo indeksin : {result} ve kilo değerlendirmen {kilolu}")
print(f"{name} kilo indeksin : {result} ve kilo değerlendirmen {obez}")