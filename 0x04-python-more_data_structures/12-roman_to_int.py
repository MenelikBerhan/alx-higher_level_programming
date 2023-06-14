#!/usr/bin/python3
def roman_to_int(roman_string):
    '''Converts a Roman numeral to integer

    Args:
        my_list: a list used to create the new list
        number: integer to multiply values of my_list

    Returns: an integer value of the Roman numeral
    '''
    if not roman_string or (not isinstance(roman_string, str)):
        return (0)

    r_vals1 = {'M': 1000, 'D': 500, 'C': 100, 'L': 50, 'X': 10, 'V': 5, 'I': 1}
    r_vals2 = {'CM': 900, 'CD': 400, 'XC': 90, 'XL': 40, 'IX': 9, 'IV': 4}
    temp_roman = roman_string[:]
    deci = 0
    for i in r_vals2:
        deci += temp_roman.count(i) * r_vals2[i]
    for i in r_vals2:
        temp_roman = temp_roman.replace(i, "")
    for i in r_vals1:
        deci += temp_roman.count(i) * r_vals1[i]
    return (deci)
