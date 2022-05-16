# İÇ İÇE FONKSİYONLAR

def factorial(number):

    if not number >= 0:
        raise Exception("Number must be an pozitif number") 

    if not isinstance(number,int):
        Exception("Number must be a number")
    
    def inner_factorial(number):
        if number <= 1:
            return 1
        
        return number * inner_factorial(number - 1)
    return inner_factorial(number)

print(factorial(6))

# FONKSİYONDAN FONKSİYON DÖNDÜRME

def usAlma(num):

    def inner_us(num2):
        return num ** num2

    return inner_us

three = usAlma(3)
print(three(3))

def yetki_sorgula(page):
    
    def inner_yetki(role):
        if role == "Admin":
            return f"{role} rolü {page} sayfasına ulaşabilir. "
        else:
            return f"{role} rolü {page} sayfasına ulaşamaz. "
    return inner_yetki

user1 = yetki_sorgula("Ayarlar")
print(user1("Admin"))
print(user1("User"))

# FONKSİYONA PARAMETRE OLARAK FONKSİYON GÖNDERME

def toplama(a,b):
    return a+b

def cikarma(a,b):
    return a-b

def carpma(a,b):
    return a*b

def bolme(a,b):
    return a/b
 
def islem(f1, f2, f3, f4, islem_adi):
    if islem_adi == "toplama":
        print(f1(2,3))

    elif islem_adi == "cikarma":
        print(f2(4,5))

    elif islem_adi == "carpma":
        print(f3(5,6))

    elif islem_adi == "bolme":
        print(f4(7,8))

    else:
        return "Geçersiz işlem"

islem(toplama,cikarma,carpma,bolme,"toplama")
islem(toplama,cikarma,carpma,bolme,"cikarma")
islem(toplama,cikarma,carpma,bolme,"carpma")
islem(toplama,cikarma,carpma,bolme,"bolme")
islem(toplama,cikarma,carpma,bolme,"toplamaaa")

# Decorator Fonksiyon

import math
import time

def calculate_time(func):
    def inner(*args, **kwargs):
        
        start = time.time()
        time.sleep(1)

        func(*args, **kwargs)

        finish = time.time()
        print(f"Fonksiyon {str(finish - start)} saniye sürdü.")
    
    return inner

@calculate_time
def usAlma(a,b):
    print(math.pow(a,b))

@calculate_time
def factorial(num):
    print(math.factorial(num))

usAlma(2,3)
factorial(4)