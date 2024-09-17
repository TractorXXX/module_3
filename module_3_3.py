def print_params(a = 1, b = 'строка', c = True):
    print(a, b, c)
#--------------------------------------------------------

print_params()
print_params(b = 25)
print_params(c = [1, 2, 3])

values_list = [11, 'aa', [3, 2, 1]]
values_dict = {'a': 22, 'b': 'bb', 'c': [6, 5, 4]}

print_params(*values_list)
print_params(**values_dict)

values_list_2 = [132, 'Python']
print_params(*values_list_2, 42)