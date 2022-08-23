#****** Sayfa Sonunda güncelleme yapma

with open("newfile.txt","a",encoding="utf-8") as file:
    file.write("Furkan Korkmaz")


with open("newfile.txt","r",encoding="utf-8") as file:
    content = file.read()
    print(content)

#********* Sayfa Başına Güncelleme Yapma

with open("newfile.txt","r+",encoding="utf-8") as file:
    file.seek(0)
    file.write("Alperen Şengün")

with open("newfile.txt","r",encoding="utf-8") as file:
    content = file.read()
    print(content)

#********* Sayfa Ortasına Güncelleme Yapma

with open("newfile.txt","r+",encoding="utf-8") as file:
    list = file.readlines()
    list.insert(2,"Hidayet Türkoğlu\n")
    file.seek(0)
    file.writelines(list)

with open("newfile.txt","r",encoding="utf-8") as file:
    content = file.read()
    print(content)
