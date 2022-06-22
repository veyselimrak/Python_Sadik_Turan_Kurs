import re

str = "Merhaba Python Programlama Kursu"
#findall

# print(re.findall("Python",str))
print(re.findall("^M",str))#ne ile başlıyor.
print(re.findall("u$",str))#ne ile bitiyor.
print(re.findall("Py",str))

#split

print(re.split(" ",str))
print(re.split("a",str))

#sub

print(re.sub(" ","-",str))
print(re.sub("a","e",str))

#search

print(re.search("[a]",str))
print(re.search("[a-z]",str))
print(re.search("[0-9]",str))





