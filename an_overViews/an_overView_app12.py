
numbers = [1,3,5,7,9,12,19,21]

i = 0
elemanSayisi = len(numbers)
while elemanSayisi != i :
    print(numbers[i])
    i = i + 1
number1 = int(input("1.Sayıyı Giriniz :"))
number2 = int(input("2.Sayıyı Giriniz :"))

if number1 > number2:
    while number2 < number1:
        if number2 % 2 == 1:
            print(number2)
        number2 = number2 + 1
else:
        while number1 < number2:
            if number1 % 2 == 1:
                print(number1)
            number1 = number1 + 1
x = 100
while x > 0:
    print(x)
    x -=1

numbers = []
i=0

while i < 5:
    
    numbers.append(int(input("Sayıları Giriniz : ")))
    i += 1
numbers.sort()

print(numbers)

from unicodedata import name


urunSayisi = int(input("Urun Adedini Giriniz :"))

urunler = []
k = 0
while k < urunSayisi:
    name  = input("Ürün Adını Giriniz :")
    price = input("Ürün Fiyatını Giriniz : ")
    urunler.append
    (
        {
            "name":name,
            "price":price
        }
    )
    k +=1
for urun in urunler:
    print(f"Ürün Adı : {urun['name']} ürün fiyatı : {urun['price']}")

#DİCTİONARY DE LİSTELEME YAPARKEN PRİNT KOMUTUNDA TEK TIRNAK KULLANILIYORSA AD DA TEK KULLANILIR AYNI ŞEKİLDE KULLANILMAMASI GEREKİR.







    
