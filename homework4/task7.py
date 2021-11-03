import math


def fact(n):
    for i in range(1, n+1):
        yield math.factorial(i)


num = int(input('Input end number for factorial: '))
for el in fact(num):
    print(el)

