def get_multipliend_digits(number):
    str_number = str(number)
    first = int(str_number[0])
    if len(str_number) > 1:
        return first * get_multipliend_digits(int(str_number[1:]))
    else:
        return first


result = get_multipliend_digits(40203)
print(result)