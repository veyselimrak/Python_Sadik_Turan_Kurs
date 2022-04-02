#Inheritance (Kalıtım) : Miras Alma

class Person():
    def __init__(self, fname, lname):
        self.firstName = fname
        self.lastName = lname
        print("Person Created")

    def who_am_i(self):
        print("I am a Person")

    def eat(self):
        print("I am eating")

class Student(Person):
    def __init__(self, fname, lname, number):
        self.studentNumber = number
        Person.__init__(self, fname, lname)
        print("Student Created")
    
    #override
    def who_am_i(self):
        print("I am a Student")


class Teacher (Person):
    def __init__(self, fname, lname, branch):
        self.branch = branch
        Person.__init__(self, fname, lname)
        


    def who_am_i(self):
        print(f"I am a {self.branch} Teacher")

p1 = Person("Veysel", "İmrak")
s1 = Student("Muhyettin", "İmrak", 2123)
t1 = Teacher("Ömer", "İmrak", "Computer Engineering")

t1.who_am_i()

p1.who_am_i()
s1.who_am_i()
p1.eat()
s1.eat()

print(p1.firstName + " " + p1.lastName)
print(s1.firstName + " " + s1.lastName + " " , s1.studentNumber)


        
        