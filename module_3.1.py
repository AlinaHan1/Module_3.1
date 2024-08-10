calls = 0


def count_calls():
    global calls
    calls += 1


def string_info(x):
    count_calls()
    x = len(x), x.upper(), x.lower()
    return tuple(x)




def is_contains(string, list_to_search):
    list_to_search = [s.lower() for s in list_to_search]
    string = string.lower()
    if string in list_to_search:
        count_calls()
        return True
    else:
        count_calls()
        return False



print(string_info('Capybara'))
print(string_info('Armageddon'))
print(is_contains('UrbaN', ['ban', 'BaNaN', 'urBAN']))
print(is_contains('cycle', ['recycling', 'cyclic']))
print(calls)
