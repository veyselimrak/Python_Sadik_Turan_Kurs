from traceback import print_tb
from unicodedata import name


website = "https://www.btkakademi.gov.tr/portal/course/player/deliver/sifirdan-ileri-seviye-python-programlama-5877"
course = "Sıfırdan İleri Seviye Python Programlama Sadık Turan"

print(len(course))
print(website[8:11])
print(website[23:26])

length = len(course)

print(course[:15],"\n"+course[length-15:length])
print(course[52::-1])

name,surname,age,job = "Veysel","İmrak",22,"mühendis"

print(f"Benim Adım {name} {surname} , Yaşım {age} ve mesleğim {job}")
print("Benim Adım {} {} , Yaşım {} ve mesleğim {}".format(name,surname,age,job))


v = "Hello world"

yeniv = v[0:5] + " W" + v[7:11]
print(yeniv)



b ="abc " * 3 
print(b)
