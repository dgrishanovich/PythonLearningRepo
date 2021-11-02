import random as rnd

list_len = int(input('Enter list length: '))
init_list = [rnd.randint(0, 10) for _ in range(list_len)]
print('Init list: ', init_list)

unique_list = [x for x in init_list if init_list.count(x) == 1]
print('Unique list:', unique_list)