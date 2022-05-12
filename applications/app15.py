import random
from unicodedata import name

# result = dir(random)
# result = help(random)


result = random.random()
result = int(random.uniform(10,100))
result = random.randint(10,100)

names = ["Veysel" , "Yağmur" , "Deniz" , "Cenk"]

result = names[random.randint(0,len(names)-1)]

result = random.sample(names,2)

print(result)