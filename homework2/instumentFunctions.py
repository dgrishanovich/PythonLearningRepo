def inputWithType(inputKey):
    strInput = input("Input product " + inputKey + ": ")
    if inputKey == 'Number':
        return int(strInput)
    elif inputKey == 'Price':
        return float(strInput)
    else:
        return strInput