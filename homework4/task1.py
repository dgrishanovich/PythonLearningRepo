from sys import argv


def count_salary(worked_hours, hour_rate, bonus):
    return worked_hours*hour_rate + bonus


_, worked_hours_param, hours_param, bonus_param = argv
print(f'Money earned: {count_salary(float(worked_hours_param), float(hours_param), float(bonus_param))}')

