#4
def default_power(x, y):
    return x**y

def power_with_loop(x, y):
    res = 1.0
    for i in range(abs(y)):
        res /= x
    return res


x = float(input("Input float positive number: "))
y = int(input("Input integer negative power: "))
print(f'Using ** operator: {default_power(x, y)}')
print(f'Using loop: {power_with_loop(x, y)}')