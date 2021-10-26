import random as rnd

randomLst = [rnd.randint(0, 9) for _ in range(5)]
randomLst.sort(reverse=True)
print(randomLst)
newInt = int(input('Input new integer: '))
randomLst.append(newInt)
randomLst.sort(reverse=True)
print(randomLst)
