import numbers
from subprocess import list2cmdline
from unittest import result


def square(num): return num ** 2
square = lambda num: num ** 2

numbers = [1,3,5,9]

result = list(map(lambda num: num ** 2,numbers))
result = list(map(square, numbers))

result = square(3)

for item in map(square, numbers):
    print(item)



print(result)