dict_numbers = {"1": "Один", "2": "Два", "3": "Три", "4": "Четыре"}

data = []
with open("files/initial_file_for_task4.txt", "r") as file_for_read:
    for line in file_for_read:
        key, value = line.split(" — ")
        x = line.replace(key.strip(), dict_numbers[value.strip()])
        data.append(x)
with open("new_file_for_task_4.txt", "w") as created_file:
    created_file.writelines(data)