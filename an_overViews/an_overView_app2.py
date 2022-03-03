from traceback import print_tb


course = "Sıfırdan İleri Seviye Python Programlama Sadık Turan "
website = "https://www.btkakademi.gov.tr/portal/course/player/deliver/sifirdan-ileri-seviye-python-programlama-5877"

course = course.lower()

print(course)

a = website.count("a")
print(a)

print(website.startswith("https"))
print(website.endswith("com"))

print(website.find("gov"))
print(website.find("com"))

print(course.isalpha())

c = "Contents"


cc = "Contents".center(50,"*")
print(cc)

d = course.replace(" ","-")
print(d)

f = "Hello World"
print(f.replace("World","There"))

ff = course.split(" ")
print(ff)

print(ff[2])