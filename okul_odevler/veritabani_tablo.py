import sqlite3
#Veri Tabanına Dışarıdan Veri Girişi

vt = sqlite3.connect("veriTabani2.db")

imlec = vt.cursor()

imlec.execute("CREATE TABLE IF NOT EXISTS Users (ID Integer, ad, soyad, memleket)")


imlec.execute("INSERT INTO Users VALUES('1', 'Süleyman', 'UZUN', 'Yazılımcı')")
Ad = []
Soyad = []
Memleket = []
idler = []

for id in range(2,5):
    idler.append(id)

for i in range(0,3):
    ad = input("Ad Giriniz: ")
    Ad.append(ad)

for i in range(0,3):
    soyad = input("Soyad Giriniz: ")
    Soyad.append(soyad)

for i in range(0,3):
    memleket = input("Memleket Giriniz: ")
    Memleket.append(memleket)
veriler =[]
for i in range(0,3):
    veri = (idler[i], Ad[i], Soyad[i], Memleket[i])
    veriler.append(veri)


for veri in veriler:
    imlec.execute(f"""INSERT INTO Users VALUES(?, ?, ?, ?)""",veri)




vt.commit()
vt.close()
 
