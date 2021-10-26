import random as rnd

lst = [x for x in range(10)]
print(lst)

randomLst = [rnd.uniform(0, 10) for _ in range(5)]
print(randomLst)

stringLst = [str(x) for x in range(20, 27)]
print(stringLst)

resultList = []
resultList.extend(lst)
resultList.extend(stringLst)
resultList.extend(randomLst)

print('Types of result list elements:')
for element in resultList:
    print(type(element))