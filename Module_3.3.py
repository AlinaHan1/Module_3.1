def print_params(a=1, b='string', c=True):
    print(a, b, c)


values_list = [{'H', 'i', ',', 't', 'i', 'c', 'h', 'e', 'r'}, 'Module', 3.3]
values_list_2 = [26, ['a', 'p', 'r', 'i', 'l']]
values_dict = {'a': 26, 'b': 'april', 'c': 1989}

print_params()
print_params(4, 'string', False)
print_params(b=25)
print_params(c=[1, 2, 3])
print_params(*values_list)
print_params(*values_list_2, 1989)
print_params(**values_dict)
