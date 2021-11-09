# Task 6
import re


def regex_remove_brackets(s):
    pattern = r"\([^()]*\)"
    t = re.sub(pattern, '', s)
    return t


dict_subjects = {}
with open("files/file_for_task6.txt", "r") as file_for_read:
    for line in file_for_read:
        key, value = line.split(":")
        st = value.replace("—", "").replace(".", "").strip()
        dict_subjects[key.strip()] = sum(list(map(int, regex_remove_brackets(st).split())))
print(dict_subjects)