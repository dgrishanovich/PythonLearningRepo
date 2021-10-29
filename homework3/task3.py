def my_func(num1, num2, num3):
    listNumbers = [num1, num2, num3]
    min1 = min(listNumbers)
    listNumbers.remove(min1)
    print(listNumbers)
    return sum(listNumbers)


num1, num2, num3 = [float(x) for x in input('Input 3 numbers: ').split()]
print(my_func(num1, num2, num3))
