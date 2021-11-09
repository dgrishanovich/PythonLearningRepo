# Task 1
file_name = input("Enter file name that will be created in current directory: ")

with open(file_name+".txt", "w") as created_file:
    for line in iter(input, ''):
        created_file.write(line + '\n')

