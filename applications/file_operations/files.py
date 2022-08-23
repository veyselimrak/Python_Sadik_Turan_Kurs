# Dosya İşlemleri
# "w" özelliği dosya oluşturur ve içine yazma işlemi yaapar. eğer önceden bir dosya varsa ise o dosyayı siler ve yenisini oluşturur.

file = open("file.txt","w",encoding="utf-8")
file.write("Veysel İmrak")
file = open("file.txt","w",encoding="utf-8")
file.write("Yazılım Kafası")
file.close()

# "a" özelliği Dosya yoksa oluşturur. Önceden dosya oluşturulmuş ise üstüne ekleme işlemi yapılur.

file1 = open("file1.txt","a",encoding="utf-8")
file1.write("Veysel İmrak\t")
file1 = open("file1.txt","a",encoding="utf-8")
file1.write("Yazılım Kafası\n")
file1.close()

# "x" özelliği Dosya oluşturur. Önceden dosya oluşturulmuş ise hata verir.
# "r" özelliği dosya okuma işlemi yapar.

file2 = open("file2.txt","x",encoding="utf-8")
file2.write("Veysel İmrak\t")
file2.close()






