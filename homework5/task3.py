# Task 3
from statistics import mean

dict_surname_salary = {}
with open("files/file_for_task3.txt", "r") as file_for_read:
    for line in file_for_read:
        key, value = line.split()
        dict_surname_salary[key] = int(value)
print(dict_surname_salary)

little_surnames = [surname for surname, salary in dict_surname_salary.items() if int(salary) < 20000]
print("Surnames with salary < 20000:", little_surnames)

avg_salary = mean(dict_surname_salary.values())
print('The average salary is: ', avg_salary)