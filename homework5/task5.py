import random as rnd
initial_list = [rnd.randint(0, 30) for _ in range(10)]
file_with_numbers = open("created_file_for_task5.txt", "w+")
for num in initial_list:
    file_with_numbers.write(str(num) + " ")
file_with_numbers.seek(0)
file_sum = 0
numbers_read_from_file = list(map(int, file_with_numbers.read().split()))
file_with_numbers.close()
print(sum(numbers_read_from_file))
