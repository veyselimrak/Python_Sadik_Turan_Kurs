
numbers = [1,3,5,7,9,12,19,21]
toplam = 0
for number in numbers:
    if number % 3 == 0:
        print(f"{number} sayısı 3'ün katıdır.")
    if number % 2 != 0:
            print(number ** 2)
    toplam = toplam + number
print(toplam)

sehirler = [ "kocaeli","istanbul","ankara","izmir","rize" ]

for sehir in sehirler:
    if len(sehir) < 6:
        print(f"{sehir} adlı şehir en fazla 5 karakterlidir.")

urunler = [
    {"name":"SamsungS6","price":"3000"},
    {"name":"SamsungS7","price":"4000"},
    {"name":"SamsungS8","price":"5000"},
    {"name":"SamsungS9","price":"6000"},
    {"name":"SamsungS10","price":"7000"}
]
toplam = 0  
for urun in urunler:
    fiyat = int(urun["price"])
    toplam = toplam + fiyat
print("Ürünleri Fiyatları Toplamı : ",toplam)

for fiyat in urunler:
    if int(fiyat["price"]) > 5000:
        print(fiyat)
