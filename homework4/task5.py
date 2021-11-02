from functools import reduce

init_list = [x for x in range(100, 1001) if x % 2 == 0]
print(init_list)

print(reduce(lambda a, b: a * b, init_list))