# Task 7
from statistics import mean
import json
profit_list = []
firm_dict = {}
with open("files/file_for_task7.txt", "r") as companies_file:
    for line in companies_file:
        firm_data = line.strip().split()
        profit = int(firm_data[2]) - int(firm_data[3])
        profit_list.append(profit)
        firm_dict[firm_data[0]] = profit
average_profit_value = mean([x for x in profit_list if x > 0])
average_profit_dict = {'average_profit': average_profit_value}
print("Companies profit:", profit_list)
print("Average profit = ", average_profit_value)
result_list = [firm_dict, average_profit_dict]
print(result_list)

with open("result_file_task7.json", "w") as write_file_json:
    json.dump(result_list, write_file_json)

