proceeds = float(input("Input proceeds of the company: "))
costs = float(input("Input costs of the company: "))

if proceeds > costs:
    print("Profit!")
    profit = proceeds - costs
    proceedsProfitability = profit / proceeds
    print("Proceeds profitability =", proceedsProfitability)
    employeeNumber = int(input("Please input the current number of company employees: "))
    print("Profit per employee =", profit / employeeNumber)
else:
    print("Loss...")