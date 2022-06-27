# #class

# class Person:
#     #class attributes(Öznitelikler)
#     address = "no information"
#     #object attributes
#     #constructor(yapıcı metot)
#     def __init__(this, name, year):
#         this.name = name
#         this.year = year
#     #instance methods(objelere özel metotlar)
#     def intro(this):
#         print("HELLO THERE " + this.name)
#     def calculateAge(this):
#         return 2019 - this.year

# p1 =Person("Veysel", 2000)
# p2 = Person("Muhammet", 1996)
# #accesing objecct 

# p1.name = "ahmet"
# p1.address = "Kartal"
# p2.address = "Gümüşpınar"
# print(f"yaşınız : {p1.calculateAge()}")
# print(f"yaşınız : {p2.calculateAge()}")

# print(f"p1 name : {p1.name} year : {p1.year} address : {p1.address}")
# print(f"p2 name : {p2.name} year : {p2.year} address : {p2.address}")

# p1.intro()



class Circle:
    #Class object attribute
    pi = 3.14

    def __init__(this, yaricap=1):
        this.yaricap = yaricap

    #Methods
    def cevreHesapla(this):
        return 2*this.pi * this.yaricap
    def alanHesapla(this):
        return this.pi * (this.yaricap **2)

c1 = Circle()
c2 = Circle(5)

print(f"c1 : alan = {c1.alanHesapla()} Çevre : = {c1.cevreHesapla()}")
print(f"c2 : alan = {c2.alanHesapla()} Çevre : = {c2.cevreHesapla()}")
