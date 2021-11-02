import random as rnd

list_len = int(input('Enter list length: '))

initial_list = [rnd.randint(0, 30) for _ in range(list_len)]
print(initial_list)


new_list = [i for idx, i in enumerate(initial_list) if (idx > 0) & (i > initial_list[idx - 1])]
print(new_list)