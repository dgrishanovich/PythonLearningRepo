def division(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return 'Division by 0!'


numerator, denominator = [float(x) for x in input('Input a, b: ').split()]
print(division(numerator, denominator))
