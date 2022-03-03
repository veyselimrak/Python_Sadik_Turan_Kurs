from operator import le
from os import remove
from traceback import print_tb

cars = ["Mazda","Opel","BMW","Mercedes"]

print(len(cars))
print(cars[0] + " " + cars[3])
print(cars[0].replace("Mazda","Toyota"))
print(cars[-2])
print("Mercedes" in cars)

ilk3 = cars[0] + cars[1] + cars[2]

print(ilk3)
print(cars[0:3])
cars[2:4] = ["Toyota","Renault"]
print(cars)

cars.append("Audi")
cars.append("Nissan")
cars.remove("Renault")
del cars[-1]
print(cars)
print(cars)
print(cars[::-1])

studentA = ["Yiğit Bilgi  ",2010, (70,60,70)]
studentB = ["Sena Turan ",1999,(80,80,70)]
studentC = ["Ahmet Turan ",1998,(80,70,90)]

students = (studentA,studentB,studentC)
print(students)

print(f"{studentA[0]} {2022-studentA[1]} yaşında ve not ortalaması {(studentA[2][0]+studentA[2][1]+studentA[2][2])/3}")

print(f"{studentB[0]} {2022-studentB[1]} yaşında ve not ortalaması {(studentB[2][0]+studentB[2][1]+studentB[2][2])/3}")
 
print(f"{studentC[0]} {2022-studentC[1]} yaşında ve not ortalaması {(studentC[2][0]+studentC[2][1]+studentC[2][2])/3}")