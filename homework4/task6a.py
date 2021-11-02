from itertools import count
from sys import argv

_, start, end = argv
i_start, i_end = int(start), int(end)
for i in count(i_start):
    print(i)
    if i == i_end:
        break
