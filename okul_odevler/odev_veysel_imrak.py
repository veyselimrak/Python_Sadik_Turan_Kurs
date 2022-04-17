from operator import le
import pstats
import string

class User_Registration():

    def __init__(self, userName, password):
        self.password = password
        self.userName = userName
        
    def rakamControl(self, userName, password):
        rakamlar = "0123456789"
        for rakam in rakamlar:
            if rakam in userName:
                
                break
        else:
            print("HATA: Kullanıcı adınıza rakam ekleyin")

        for rakam in rakamlar:
            if rakam in password:
                
                break
        else:
            print("HATA: Şifrenize rakam ekleyin")

    def lengthControl(self, userName, password):
        if len(userName) <=16:
            pass
        else:
            print("HATA: Karakter uzunluğu 16'dan kısa olmalıdır.")

        if len(password) >= 8 and len(password) <=24:
            pass
        else:
            print("HATA: Şifrenizin karakter uzunluğu 8'den büyük 24'den küçük olmalıdır.")

    def b_harf_control(self,userName, password):
        
        b_harfler = string.ascii_uppercase

        for b_harf in b_harfler:
            if b_harf in userName:
                
                break
        else:
            print("HATA: Kullanıcı adınıza en az 1 büyük harf ekleyiniz.")

        for b_harf in b_harfler:
            if b_harf in password:
                
                break
        else:
            print("HATA: Şifrenize en az 1 büyük harf ekleyiniz.")
    
    def k_harf_control(self,userName, password):
        
        k_harfler = string.ascii_lowercase

        for k_harf in k_harfler:
            if k_harf in userName:
                
                break
        else:
            print("HATA: Kullanıcı adınıza en az 1 küçük harf ekleyiniz.")

        for k_harf in k_harfler:
            if k_harf in password:
                
                break
        else:
            print("HATA: Şifrenize en az 1 küçük harf ekleyiniz.")

    def o_karakter_control(self,userName, password):
        o_karakterler = string.punctuation

        for o_karakter in o_karakterler:
            if o_karakter in userName:
                print("HATA: Kullanıcı adınızda özel karakter bulunmamalıdır.")
                break
        else:
            pass

        for o_karakter in o_karakterler:
            if o_karakter in password:
                
                break
        else:
            print("HATA: Şifrenizde en az 1  özel karakter bulunmalıdır.")
            


print("\nKullanıcı Oluşturma Kuralları :\n")
print("- Kullanıcı Adınızın  karakter uzunluğu en fazla 16 olmalıdır.\n")
print("- Kullanıcı Adınızda sadece büyük harf , küçük harf rakam içermelidir.\n")
print("- Kullanıcızı Adınızı oluştururken Türkçe karakter kullanmayınız.\n")
print("- Şifrenizin karakter uzunlıuğu en az 8 en fazla 24 olmalıdır.\n")
print("- Şifrenizde en az 1 büyük harf , küçük harf rakam ve özel karakter içermelidir.\n\n")

user1 = User_Registration("Veysel34","5377701925Ad_")
user1.rakamControl(user1.userName,user1.password)
user1.lengthControl(user1.userName,user1.password)
user1.b_harf_control(user1.userName,user1.password)
user1.k_harf_control(user1.userName,user1.password)
user1.o_karakter_control(user1.userName,user1.password)
