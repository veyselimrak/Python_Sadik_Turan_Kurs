
veyselHesap = {
    "ad":"Veysel İmrak",
    "hesapNo":"123456789",
    "hesapBakiye":3000,
    "hesapEkBakiye":2000
}


omerHesap = {
    "ad":"Ömer İmrak",
    "hesapNo":"456481234",
    "hesapBakiye":2000,
    "hesapEkBakiye":1000
}

def paraCek(hesap, miktar):
    print(f"Merhaba {hesap['ad']}")

    if hesap['hesapBakiye'] > miktar:
        hesap['hesapBakiye'] -= miktar 
        print(f"{miktar} kadar para çekildi.")
    elif hesap['hesapBakiye'] == miktar:
        print(f"{miktar} kadar para çekildi.\nHesapta paranız bitmiştir.")
    elif hesap['hesapBakiye'] < miktar:
        print(f"{miktar} kadar para hesapta bulunmamaktadır.\nEk Bakiyeyi kullanmak ister misiniz?")
        tercih = input("Evet Mi?\nHayır Mı?\nYanıtınız : ")
        
        if tercih == "Evet":
            toplam = hesap['hesapBakiye'] + hesap['hesapEkBakiye']
        
        if toplam >= miktar:
            
            bakiye = hesap['hesapBakiye']
            ekKullanilacakMiktar = miktar - hesap['hesapBakiye']
            hesap['hesapBakiye'] = 0
            hesap['hesapEkBakiye'] = ekKullanilacakMiktar
            
            print("Paranızı Alabilirsiniz.")
        else:
            print(f"Hesabınızda bulunan toplam para miktarı : {toplam}")
    else:
        print(f"Bakiyeniz yetmemektedir.\nHesabınızda bulunan para miktarı : {hesap['hesapBakiye']} ")

def bakiyeSorgulama(hesap):
    print(f"{hesap['hesapNo']} Nolu hesapta bulunan para miktarı : {hesap['hesapBakiye']} ek hesap miktarı : {hesap['hesapEkBakiye']}" )



paraCek(veyselHesap, 2500)
bakiyeSorgulama(veyselHesap)
paraCek(veyselHesap, 2000)