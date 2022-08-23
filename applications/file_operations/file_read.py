try:
    file = open("newfile.txt","r")
    print(file)
except FileNotFoundError :
    print("Dosya Okuma Hatası")

finally:
    print("Dosya Kapandı.")
    file.close()


# ****** read() fonksiyonu ile okuma işlemi yapar. Uzunlukta belirtilebilir.

file = open("newfile.txt","r",encoding="utf-8")

content = file.read()

print(content)

#********radline()fonksiyonu satır satır okuma işlemi yapar.
file = open("newfile.txt","r",encoding="utf-8")

print(file.readline(),end=" ")
print(file.readline(),end=" ")
print(file.readline(),end=" ")
print(file.readline(),end=" ")


#******** readlines() fonksiyonu ile dizi oluşturup satırdaki elemanları dizi elemanı olarak alır.

file = open("newfile.txt","r",encoding="utf-8")

content = file.readlines()

print(content)

file.close()    