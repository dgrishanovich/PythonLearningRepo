#5
def list_contains_spec_symbol(lst, spec_symbol="Q"):
    return spec_symbol in (token.upper() for token in lst)


def numbers(lst):
    return [int(token) for token in lst if token.isdigit()]


should_exit = False
current_sum = 0
while not should_exit:
    input_list = [x for x in input('Input numbers: ').split()]
    current_sum += sum(numbers(input_list))
    print(f'Current sum = {current_sum}')
    should_exit = list_contains_spec_symbol(input_list)