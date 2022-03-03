from traceback import print_tb


website = "https://www.youtube.com/channel/UC-9-kyTW8ZkZNDHQJ6FgpwQ"

course = "Veysel Python Kursuna başlıyor. Hedef Ben miyim Tayfun.:)"

a = course.split(" ")

print(a)
print(course.replace(" ","-"))

name = "Veysel İmrak"
yas = 22

print(name.center(50,"*"))
print(website.find("www"))
print(website.startswith("htt"))
print(website.startswith("wwww"))
print(course.endswith(":)"))
print(course.endswith("un"))
print(course.count("e"))
print(website[8:11])
print(website[8:30:2])
print(len(website))
print(website[len(website)::-1])
print(course[len(course)::-1])
print(name.replace("Veysel","Muhammet"))

print(f"Benim Adım {name} ve Yaşım {yas} ")
print("Benim Adım {} ve Yaşım {}".format(name,yas))




