
for x in range(0,10,2):
    print(x)



name = "Veysel"

for index,letter in enumerate(name):
    print(f"{index} index numaralı değer : {letter}")

list1 = [0,1,2,3]
list2 = ["Veysel","Muhammet","Ömer","Muhyettin"]

for index,name in zip(list1,list2):
    print(f"{index} numaralı değer : {name}")
