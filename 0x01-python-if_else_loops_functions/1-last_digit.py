#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number < 0:
    lst_dgt = -(-number % 10)
else:
    lst_dgt = number % 10
if lst_dgt > 5:
    print(f"Last digit of {number} is {lst_dgt} and is greater than 5")
elif lst_dgt == 0:
    print(f"Last digit of {number} is {lst_dgt} and is 0")
else:
    print(f"Last digit of {number} is {lst_dgt} and is less than 6 and not 0")
