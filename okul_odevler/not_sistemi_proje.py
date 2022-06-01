
def hata_yonetimi(func):

    def inner():
        while True:
            try:
                func()
            except Exception as ex:
                print(f"Hatalı Giriş Yaptınız.\nHata Mesajı:{ex}\nLütfen Tekrar Deneyiniz. ")
            else:
                break
        return "Sistem Başarıyla Tamamlanmıştır."    
    return inner()

@hata_yonetimi
def bolum():
    bolumler = []
    bolum_sayisi = int(input("Lütfen Bölüm Sayısını Giriniz: "))
    for i in range(0,bolum_sayisi):
        bolum_adi = input(f"Lütfen {i+1}. Bölümün Adını Giriniz: ")
        bolumler.append(bolum_adi)

    def ders():
        for y in range(0,bolum_sayisi):
            ders_sayilari = []
            ders_sayisi = int(input(f"Lütfen {bolumler[y]} bölümü için ders sayısı giriniz: "))
            ders_sayilari.append(ders_sayisi)
            dersler = []
            for x in range(0,ders_sayisi):
                ders_adi = input(f"Lütfen {bolumler[y]} bölümü için {x + 1}. dersi Giriniz: ")
                dersler.append(ders_adi)
            bolumler[y] = dersler

        def degerlendirme():
            degerlendirmeler = []
            agirlik_yuzdeleri = []
            degerlendirme_sayilari = []
            for i in range(0,len(bolumler)):
                        
                    for k in range(0,len(bolumler[i])):
                        degerlendirme_sayisi = int(input(f"Lütfen {bolumler[i][k]} Dersi için  Değerlendirme Sayısını Giriniz: "))
                        degerlendirme_sayilari.append(degerlendirme_sayisi)
                        for z in range(0,degerlendirme_sayisi):

                            degerlendirme_adi = input(f"Lütfen {bolumler[i][k]} dersi için {z + 1}. değerlendirme adını giriniz: ")
                            degerlendirmeler.append(degerlendirme_adi)
                            agirlik_yuzdesi_adi = float(input(f"Lütfen {bolumler[i][k]} dersi için {z + 1}. ağırlık yüzdesi giriniz: "))
                            agirlik_yuzdeleri.append(agirlik_yuzdesi_adi)

            def ogrenciBilgileri():
                ogrenci_adlari = []
                ogrenci_numaralari = []
                ogrenci_sayilari = []

                for i in range(0,len(bolumler)):
                        
                    for k in range(0,len(bolumler[i])):
                        
                        while True: 
                            ogrenci_sayisi = int(input(f"Lütfen {bolumler[i][k]} Dersi için  Öğrenci Sayısını Giriniz: "))
                            if ogrenci_sayisi >= 5  and ogrenci_sayisi <= 20:
                                ogrenci_sayilari.append(ogrenci_sayisi)
                                for z in range(0,ogrenci_sayisi):

                                    ogrenci_adi = input(f"Lütfen {bolumler[i][k]} dersi için {z + 1}. öğrencinin adını giriniz: ")
                                    ogrenci_adlari.append(ogrenci_adi)
                                    ogrenci_numara = int(input(f"Lütfen {bolumler[i][k]} dersi için  {z + 1}. öğrencinin numarasını giriniz: "))
                                    ogrenci_numaralari.append(ogrenci_numara)

                                break
                            else:
                                print("Öğrenci sayısı 5'den büyük 20'den küçük olmalıdır.\nLütfen Tekrar Giriniz.")

                def not_ortalama():
                    not_ortalamalari = []           
                    for i in range(0,len(bolumler)):
                        for k in range(0,len(bolumler[i])):
                            hedef = degerlendirme_sayilari[k]
                            for z in range(0,ogrenci_sayilari[k]):
                                not_ortalamasi = 0
                                for x in range(0,hedef):
                                    while True:
                                        sinav_notu = float(input(f"Lütfen {z+1}. öğrencinin {bolumler[i][k]} dersinin {degerlendirmeler[x]} değerlendirmesi için Not Giriniz:   "))
                                        if sinav_notu <= 100 and sinav_notu >= 0:
                                            not_ortalamasi = not_ortalamasi + (sinav_notu * agirlik_yuzdeleri[x])
                                            break
                                        else:
                                            print("Sınav Notu 0 ile 100 aralığında olması gerekir.")
                                not_ortalamalari.append(not_ortalamasi)
                                print(f"{bolumler[i][k]} dersinin {ogrenci_adlari[z]} adlı öğrencinin not ortalaması: {not_ortalamalari[z]} ")
                    
                    for i in range(0,10):
                        print(ogrenci_adlari[i],ogrenci_numaralari[i] ,not_ortalamalari[i])
                    

                    def not_sistemi():
                        harf_notlari= []
                        dortluk_notlar = []
                        for i in range(0,len(not_ortalamalari)):
                            gecici_not = not_ortalamalari[i]
                            if gecici_not <= 100 and gecici_not >= 90:
                                harf_notu = "AA"
                                harf_notlari.append(harf_notu)
                                dortluk_not = 4.0
                                dortluk_notlar.append(dortluk_not)
                            if gecici_not <= 89 and gecici_not >= 85:
                                harf_notu = "BA"
                                harf_notlari.append(harf_notu)
                                dortluk_not = 3.5
                                dortluk_notlar.append(dortluk_not)
                            if gecici_not <= 84 and gecici_not >= 80:
                                harf_notu = "BB"
                                harf_notlari.append(harf_notu)
                                dortluk_not = 3.0
                                dortluk_notlar.append(dortluk_not)
                            if gecici_not <= 79 and gecici_not >= 75:
                                harf_notu = "CB"
                                harf_notlari.append(harf_notu)
                                dortluk_not = 2.5
                                dortluk_notlar.append(dortluk_not)
                            if gecici_not <= 74 and gecici_not >= 70:
                                harf_notu = "CC"
                                harf_notlari.append(harf_notu)
                                dortluk_not = 2.0
                                dortluk_notlar.append(dortluk_not)
                            if gecici_not <= 69 and gecici_not >= 65:
                                harf_notu = "DC"
                                harf_notlari.append(harf_notu)
                                dortluk_not = 1.5
                                dortluk_notlar.append(dortluk_not)
                            if gecici_not <= 64 and gecici_not >= 60:
                                harf_notu = "DD"
                                harf_notlari.append(harf_notu)
                                dortluk_not = 1.0
                                dortluk_notlar.append(dortluk_not)
                            if gecici_not <= 59 and gecici_not >= 50:
                                harf_notu = "FD"
                                harf_notlari.append(harf_notu)
                                dortluk_not = 0.5
                                dortluk_notlar.append(dortluk_not)
                            if gecici_not <= 49 and gecici_not >= 0:
                                harf_notu = "FF"
                                harf_notlari.append(harf_notu)
                                dortluk_not = 0.0
                                dortluk_notlar.append(dortluk_not)

                        for x in range(0,len(harf_notlari)):
                            print(f"{ogrenci_adlari[x]} adlı {ogrenci_numaralari[x]} numaralı öğrencinin harf notu: {harf_notlari[x]} dortluk sistemde notu: {dortluk_notlar[x]}")

                        def guncelleme():
                            
                            tercih = int(input("Güncelleme Yapmak İster Misiniz?\nEvet : 1 Hayır : 2\n: "))
                            if not tercih == 1 and not tercih == 2:
                                raise Exception("Lütfen 1 veya 2  giriniz.")
                            elif tercih == 2:
                                quit()
                            else:
                                print(
                                    """
                                    1:Öğrenci Adı Güncellemesi
                                    2:Öğrenci Numara Güncellemesi
                                    3:Öğrenci Not Güncelleme
                                    4:Değerlendirme Adı Güncelleme
                                    5:Değerlendirme Ağırlık Yüzdesi Güncelleme
                                    6:Öğrenci adı silme
                                    7:Öğrenci numara silme
                                    8:Öğrenci Not Silme
                                    9:Değerlendirme Adı Silme
                                    10:Değerlendirme Ağırlık Yüzdesi Silme
                                    """
                                )
                                
                                secim = int(input("Seçiminizi Tuşlayınız: "))
                                if secim == 1 or secim == 2 or secim == 3 or secim == 4 or secim == 5 or secim == 6 or secim == 7 or secim == 8 or secim == 9 or secim == 10:
                                    pass
                                else:
                                    raise ValueError("Lütfen geçerli bir değer  giriniz.")
                            def ogr_adi_gncllm():
                                ad = input("Değiştirilecek Ad: ")
                                if ad in ogrenci_adlari:
                                    index = ogrenci_adlari.index(ad)
                                    ogrenci_adlari[index] = input("Girmek İstediğiniz İsmi Giriniz: ")
                                    return "İsim Başarıyla değiştirilmiştir."
                                else:
                                    print("Böyle bir ad bulunmamaktadır.")

                            def ogr_numr_gncllm():
                                numara = int(input("Değiştirilecek Numara: "))
                                if numara in ogrenci_numaralari:
                                    index = ogrenci_numaralari.index(numara)
                                    ogrenci_numaralari[index] = int(input("Girmek İstediğiniz Numarayı Giriniz: "))
                                    return "Numara Başarıyla değiştirilmiştir."
                                else:
                                    print("Böyle bir numara bulunmamaktadır.")

                            def ogr_not_gncllm():
                                ad = input("Notunu Değiştirmek istediğiniz öğrencinin Adı: ")
                                if ad in ogrenci_adlari:
                                    index = ogrenci_adlari.index(ad)
                                    not_ortalamalari[index] = int(input("Girmek İstediğiniz Adı Giriniz: "))
                                    return "Not Başarıyla değiştirilmiştir."
                                else:
                                    print("Böyle bir not bulunmamaktadır.")

                            def dgrlndrme_adi_gncllm():
                                d_adi = input("Değiştirilecek Değerlendirme Adı: ")
                                if d_adi in degerlendirmeler:
                                    index = degerlendirmeler.index(d_adi)
                                    degerlendirmeler[index] = input("Girmek İstediğiniz Değerlendirme Adını Giriniz: ")
                                    return "Değerlendirme Adı Başarıyla değiştirilmiştir."
                                else:
                                    print("Böyle bir değerlendirme adı bulunmamaktadır.")

                            def dgrlndrme_agrlk_yzds_gncllm():
                                a_yuzde = input("Ağırlık Yüzdesini Değiştirmek istediğiniz değerlendirmenin Adı: ")
                                if a_yuzde in degerlendirmeler:
                                    index = degerlendirmeler.index(a_yuzde)
                                    agirlik_yuzdeleri[index] = float(input("Girmek İstediğiniz Ağırlık Yüzdesini Giriniz: "))
                                    return "Ağırlık Yüzdesi Başarıyla değiştirilmiştir."
                                else:
                                    print("Böyle bir ağırlık yüzdesi bulunmamaktadır.")   

                            def ogr_ad_silme():
                                ad = input("Silinecek Ad: ")
                                if ad in ogrenci_adlari:
                                    index = ogrenci_adlari.index(ad)
                                    del ogrenci_adlari[index]
                                    return "İsim Başarıyla Silinmiştir."
                                else:
                                    print("Böyle bir ad bulunmamaktadır.")

                            def ogr_nmra_silme():
                                numara = int(input("Silinecek Numara: "))
                                if numara in ogrenci_numaralari:
                                    index = ogrenci_numaralari.index(numara)
                                    del ogrenci_numaralari[index]
                                    return "Numara Başarıyla Silinmiştir."
                                else:
                                    print("Böyle bir numara bulunmamaktadır.")
                            
                            def ogr_not_silme():
                                ad = input("Notunu Silmek istediğiniz öğrencinin Adı: ")
                                if ad in ogrenci_adlari:
                                    index = ogrenci_adlari.index(ad)
                                    del not_ortalamalari[index]
                                    return "Not Başarıyla Silinmiştir."
                                else:
                                    print("Böyle bir not bulunmamaktadır.")
                        
                            def dgrlndrm__ad_silme():
                                d_adi = input("Silinecek Değerlendirme Adı: ")
                                if d_adi in degerlendirmeler:
                                    index = degerlendirmeler.index(d_adi)
                                    del degerlendirmeler[index]
                                    return "Değerlendirme Adı Başarıyla Silinmiştir."
                                else:
                                    print("Böyle bir değerlendirme adı bulunmamaktadır.")

                            def dgrlndrme__agrlk_yzds_silme():
                                a_yuzde = input("Ağırlık Yüzdesini Silmek istediğiniz değerlendirmenin Adı: ")
                                if a_yuzde in degerlendirmeler:
                                    index = degerlendirmeler.index(a_yuzde)
                                    del agirlik_yuzdeleri[index]
                                    return "Ağırlık Yüzdesi Başarıyla Silinmiştir."
                                else:
                                    print("Böyle bir ağırlık yüzdesi bulunmamaktadır.") 


                            def islem(ogr_adi_gncllm,ogr_numr_gncllm,ogr_not_gncllm,
                            dgrlndrme_adi_gncllm,dgrlndrme_agrlk_yzds_gncllm,ogr_ad_silme,
                            ogr_nmra_silme,ogr_not_silme,dgrlndrm__ad_silme,dgrlndrme__agrlk_yzds_silme,secim):
                                if secim == 1:
                                    print(ogr_adi_gncllm())
                                elif secim == 2:
                                    print(ogr_numr_gncllm())
                                elif secim == 3:
                                    print(ogr_not_gncllm())
                                elif secim == 4:
                                    print(dgrlndrme_adi_gncllm())
                                elif secim == 5:
                                    print(dgrlndrme_agrlk_yzds_gncllm())
                                elif secim == 6:
                                    print(ogr_ad_silme())
                                elif secim == 7:
                                    print(ogr_nmra_silme())
                                elif secim == 8:
                                    print(ogr_not_silme())
                                elif secim == 9:
                                    print(dgrlndrm__ad_silme())
                                elif secim == 10:
                                    print(dgrlndrme__agrlk_yzds_silme())
                                print("Sistemden çıkılıyor.")
                                
                                return quit()

                            return islem(ogr_adi_gncllm,ogr_numr_gncllm,ogr_not_gncllm,
                            dgrlndrme_adi_gncllm,dgrlndrme_agrlk_yzds_gncllm,ogr_ad_silme,
                            ogr_nmra_silme,ogr_not_silme,dgrlndrm__ad_silme,dgrlndrme__agrlk_yzds_silme,secim)

                        return guncelleme()

                    return not_sistemi()

                return not_ortalama()

            return ogrenciBilgileri()

        return degerlendirme()

    return ders()

print(bolum())