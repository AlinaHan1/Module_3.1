data_structure = [[1, 2, 3], {'a': 4, 'b': 5}, (6, {'cube': 7, 'drum': 8}), 'Hello',
                  ((), [{(2, 'Urban', ('Urban2', 35))}])]


def calculate_structure_sum(data_structure):
    sum_ = []
    if isinstance(data_structure, dict):  # if data_structure == dict
        for key, value in data_structure.items():
            sum_.append(calculate_structure_sum(key))
            sum_.append(calculate_structure_sum(value))
    elif isinstance(data_structure, (list, tuple, set)):  # if data_structure == list, tuple, set
        for item in data_structure:
            sum_.append(calculate_structure_sum(item))
    elif isinstance(data_structure, int):  # if data_structure == int or float
        sum_.append(data_structure)
    elif isinstance(data_structure, str):  # if data_structure == str
        sum_.append(len(data_structure))
    return sum(sum_)


result = calculate_structure_sum(data_structure)
print(result)
