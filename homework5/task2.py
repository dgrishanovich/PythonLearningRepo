count_lines = 0
with open("files/file_for_task2.txt", "r") as file_for_read:
    for line in file_for_read:
        count_lines += 1
        words_in_line = len(line.split())
        print(f'In {count_lines} line {words_in_line} words')
    print(f'In total {count_lines} lines in file')
