inputString = [word for word in input('Input string: ').split()]
for ind, word in enumerate(inputString):
    print(ind, word[:10])