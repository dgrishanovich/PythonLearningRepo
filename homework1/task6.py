kmA = float(input("Input fist day kilometer distance: "))
kmB = float(input("Input X day kilometer distance: "))

if kmA == 0:
    print("Never")
else:
    resultDayNumber = 1
    currentDistance = kmA
    while currentDistance < kmB:
        #print("Current day: ", resultDayNumber)
        #print("Current distance", currentDistance)
        currentDistance += (currentDistance / 10)
        resultDayNumber += 1
    print(resultDayNumber)