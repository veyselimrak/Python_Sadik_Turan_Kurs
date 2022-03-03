from traceback import print_tb


names = ["Ali","Yağmur","Hakan","Deniz"]
years =  [1998,2000,1998,1987]

names.append("Cenk")
names.insert(0,"Sena")
names.remove("Deniz")

print("Ali" in names)

print(names[::-1])
print(years[::-1])

names.sort()
years.sort()

index = names.index("Hakan")
print(index)

str = "Chevrolet,Dacia"
str = str.split(",")
print(str)

print(max(years))
print(min(years))
print(years.count(1998))
years.clear()
print(years)
print(names)


markalar = []

marka = (input("Marka Adı Giriniz :"))
markalar.append(marka)
marka = (input("Marka Adı Giriniz :"))
markalar.append(marka)
marka = (input("Marka Adı Giriniz :"))
markalar.append(marka)

print(markalar)


