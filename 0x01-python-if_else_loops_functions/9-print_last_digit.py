#!/usr/bin/python3
def print_last_digit(number):
    if number < 0:
        lst_dgt = (-number % 10)
    else:
        lst_dgt = number % 10
    print(lst_dgt, end='')
    return (lst_dgt)
