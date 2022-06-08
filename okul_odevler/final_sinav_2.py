import sqlite3

vt = sqlite3.connect("veritabani.db")

im = vt.cursor()
im.execute("CREATE TABLE IF NOT EXISTS kitaplar (ad, stok_sayisi, durumu)")

im.execute("INSERT INTO kitaplar VALUES('sefiller', '100','depo')")
im.execute("INSERT INTO kitaplar VALUES('kaşağı', '200','rafta')")

im.execute("SELECT * FROM kitaplar")

veriler = im.fetchall()
print(veriler)

vt.commit()
vt.close()