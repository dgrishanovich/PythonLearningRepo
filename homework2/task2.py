input_list = [int(i) for i in input('Enter list of integers: ').split()]
new_list = []
for i, value in enumerate(input_list):
    if i % 2 == 0:
        if i < len(input_list) - 1:
            new_list.append(input_list[i+1])
        new_list.append(value)
print(new_list)