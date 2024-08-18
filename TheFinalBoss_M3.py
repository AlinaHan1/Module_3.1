data_structure = [[1, 2, 3], {'a': 4, 'b': 5}, (6, {'cube': 7, 'drum': 8}), 'Hello',
                  ((), [{(2, 'Urban', ('Urban2', 35))}])]


def calculate_structure_sum(data_structure):
    summa = 0
    if isinstance(data_structure, int):  # if data_structure == int, float
        summa += data_structure
    elif isinstance(data_structure, str):  # if data_structure == str
        summa += len(data_structure)
    elif isinstance(data_structure, dict):  # if data_structure == dict
        for key, value in data_structure.items():
            summa += calculate_structure_sum(key)
            summa += calculate_structure_sum(value)
    elif isinstance(data_structure, list):  # if data_structure == list, tuple, set
        for item in data_structure:
            summa += calculate_structure_sum(item)
    elif isinstance (data_structure, tuple):  # if data_structure == list, tuple, set
        for item in data_structure:
            summa += calculate_structure_sum(item)
    elif isinstance(data_structure, set):  # if data_structure == list, tuple, set
        for item in data_structure:
            summa += calculate_structure_sum(item)
    return summa


result = calculate_structure_sum(data_structure)
print(result)
