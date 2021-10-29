def print_user_info(name, surname, year, city, email, phone):
    lst = [name, surname, year, city, email, phone]
    s = ';'.join(lst)
    print(s)


name = input("User name: ")
surname = input("User surname: ")
year = input("User year of birth: ")
city = input("User city: ")
email = input("User email: ")
phone = input("User phone number: ")
print_user_info(name, surname, year, city, email, phone)