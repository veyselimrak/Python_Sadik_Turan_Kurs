
name = "Veysel İmrak"

for letter in name:
    if letter == "l":
        break
    print(letter)

for letter in name:
    if letter == "l":
        continue
    print(letter)







x = 0
toplam = 0

while x <= 100:
    x = x + 1
    if x % 2 == 0:
        continue
    
    toplam = toplam + x
    

print(f" Toplam : {toplam}")