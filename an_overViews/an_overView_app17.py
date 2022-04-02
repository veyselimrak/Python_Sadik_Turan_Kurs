

class Student_Registration():
    def __init__(self, fname, lname, age, number, departmant):
        self.firstName = fname
        self.lastName = lname
        self.age = age
        self.number = number
        self.departmant = departmant
        print(f"{self.firstName} {self.lastName} adlı yeni öğrenci oluşturdu.")
    
    def departmant_selection_update(self, departmant):
        print(f"Bölümünüz {departmant} olarak güncellenmiştir.")

    def delete_Registration(self, fname):
        print(f"{fname} adlı öğrencinin kayıdı silinmiştir.")


    
student1 = Student_Registration("Veysel", "İmrak", 21, 1354, "Computer Engineering")
student1.departmant_selection_update("Doctor")
student2 = Student_Registration("Ali" , "Özdemir" , 25, 1256, "Doctor")
student2.delete_Registration("Ali")
