from itertools import cycle
from sys import argv

_, input_string, stop_count = argv
i_stop = int(stop_count)
c = 0
for i in cycle(input_string):
    if c == i_stop:
        break
    print(i)
    c += 1

