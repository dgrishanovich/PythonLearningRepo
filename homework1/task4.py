strInputNumber = input('Input number:')
if strInputNumber.strip().isdigit():
    intNumber = int(strInputNumber)
    maxNumber = 0
    wholePart = intNumber
    while wholePart > 0:
        current = wholePart % 10
        if current > maxNumber:
            maxNumber = current
        wholePart = wholePart // 10
    print(maxNumber)
else:
    print("It is not a positive int number")

