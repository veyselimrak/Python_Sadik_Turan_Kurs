#def toplama(x, y):
#     z = x + y 
#     print(z)


# toplama(5,6)




# def tekrarlama(kelime, kacTekrar):
#     print(kelime * kacTekrar)
# tekrarlama("Veysel\n",2)



# def sinirsizList(*parametreler):
#     list = []

#     for parametre in parametreler:
#         list.append(parametre)

#     return list
# result = sinirsizList(10,20,30,40,50,"Veysel")

# print(result)

# def asalSayilariBulma(sayi1, sayi2):
#     for sayi in range(sayi, sayi2+1):
#         if sayi > 1:
#             for i in range(2,sayi):
#                 if (sayi % i == 0):
#                     break
#             else:
#                     print(sayi)

# sayi1 = int(input("Küçük Sayıyı Giriniz :"))
# sayi2 = int(input("Büyük Sayıyı Giriniz : "))

# asalSayilariBulma(sayi1, sayi2)



# def tamBolenleriBul(sayi):

#     tamBolenler = []

#     for i in range(2, sayi):
#         if (sayi % i == 0):
#             tamBolenler.append(i)
    
#     return tamBolenler

# print(tamBolenleriBul(40))