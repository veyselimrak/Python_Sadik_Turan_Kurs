from select import select
import string

class User_Registration():

    def __init__(self, userName, password, a):
        self.userName = userName
        self.password = password
        self.a = a
        
    def controls(self, userName, password):
        self.a = 0 
        rakamlar = "0123456789"
        for rakam in rakamlar:
            if rakam in userName:
                
                break
        else:
            print("HATA: Kullanıcı adınıza rakam ekleyin")
            self.a += 1
            
        for rakam in rakamlar:
            if rakam in password:
                self.lengthControl(self.userName,self.password)
                break
        else:
            print("HATA: Şifrenize rakam ekleyin")
            self.a += 1

    def lengthControl(self, userName, password):
         
        if len(userName) <=16:
            pass
        else:
            print("HATA: Kullanıcı Adı Karakter uzunluğu 16'dan kısa olmalıdır.")
            self.a += 1
            
        if len(password) >= 8 and len(password) <=24:
            self.b_harf_control(self.userName,self.password)
            pass
        else:
            print("HATA: Şifrenizin karakter uzunluğu 8'den büyük 24'den küçük olmalıdır.")
            self.a += 1
            
    def b_harf_control(self,userName, password,):

        b_harfler = string.ascii_uppercase

        for b_harf in b_harfler:
            if b_harf in userName:
                
                break
        else:
            print("HATA: Kullanıcı adınıza en az 1 büyük harf ekleyiniz.")
            self.a += 1
            
        for b_harf in b_harfler:
            if b_harf in password:
                self.k_harf_control(self.userName,self.password)
                break
        else:
            print("HATA: Şifrenize en az 1 büyük harf ekleyiniz.")
            self.a += 1
            
    def k_harf_control(self,userName, password):
        
        k_harfler = string.ascii_lowercase

        for k_harf in k_harfler:
            if k_harf in userName:
                
                break
        else:
            print("HATA: Kullanıcı adınıza en az 1 küçük harf ekleyiniz.")
            self.a += 1
            
        for k_harf in k_harfler:
            if k_harf in password:
                self.o_karakter_control(self.userName,self.password)
                break
        else:
            print("HATA: Şifrenize en az 1 küçük harf ekleyiniz.")
            self.a += 1
            
    def o_karakter_control(self,userName, password):
        o_karakterler = string.punctuation
        
        for o_karakter in o_karakterler:
            if o_karakter in userName:
                print("HATA: Kullanıcı adınızda özel karakter bulunmamalıdır.")
                self.a += 1
                
                break
        else:
            pass

        for o_karakter in o_karakterler:
            if o_karakter in password:
                
                break
        else:
            print("HATA: Şifrenizde en az 1  özel karakter bulunmalıdır.")


class UserLogin(User_Registration):
    def __init__(self, userName, password, a):
        super().__init__(userName, password, a),

    def userLoginControl(self, userName, password):
        if self.a == 0:
            if userName == self.userName and password == self.password:
                print("Hesaba başarıyla giriş yapıldı.\n") 
                print("Uygulamaya yönlendiriliyorsunuz.")
                self.calculator() 
            elif userName == self.userName and password != self.password:
                print("Şifrenizi yanlış girdiniz.\nLütfen tekrar deneyin.")
            elif userName != self.userName and password == self.password:
                print("Böyle bir kullanıcı adı bulunmamaktadır.\nLütfen tekrar deneyin.")
            elif userName != self.userName and password != self.password:
                print("Kullanıcı adı ve şifre yanlış!!!\nLütfen tekrar deneyin")     
            else:
                print("Hesaba Giriş yapılamadı.")
        else:
            print("Kullanıcı ve Şifrenizde Hata bulunmaktadır.\nUygulamaya giriş yapılamadı.")    
    def calculator(self):
        veri = input("İşleminizi yapınız. --> ")
        islem = eval(veri)
        print(islem)

print("\nKullanıcı Oluşturma Kuralları :\n")
print("- Kullanıcı Adınızın  karakter uzunluğu en fazla 16 olmalıdır.\n")
print("- Kullanıcı Adınız sadece büyük harf , küçük harf ve rakam içermelidir.\n")
print("- Kullanıcızı Adınızı oluştururken Türkçe karakter kullanmayınız.\n")
print("- Şifrenizin karakter uzunlıuğu en az 8 en fazla 24 olmalıdır.\n")
print("- Şifrenizde en az 1 büyük harf , küçük harf rakam ve özel karakter içermelidir.\n\n")


userName = input("Kullanıcı Adınızı Giriniz : ")
password = input("Şifrenizi Giriniz : ")

user1 = User_Registration(userName,password,0)
user1.controls(user1.userName,user1.password)
user2 = UserLogin("Adem cosşku9n",user1.password,0)
user2.userLoginControl(user1.userName,user1.password)