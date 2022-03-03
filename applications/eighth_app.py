#Değer Tipler => String , Number 
# Değişkenin Kendisi İle ilgilenilir.


x = 25
y = 10

x = y

y = 25

print(x,y)

# Referans Tipler => Class , List
# Veri tabanındaki Adres Bilgileri eşitleneceğinden aynı değişkenmiş gibi davranırlar.
# Değişkenin adresiyle ilgilenir. 

a = ["apple","banana"]
b = ["apple","banana"]

a = b

b[0] = "Lemon"

print(a,b)


