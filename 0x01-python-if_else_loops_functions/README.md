# __0x01-python-if_else_loops_functions__

## 0-positive_or_negative.py

a program that prints if a randomly generated numbers last digit is:

- zero
- less than 6
- or greater than 5.

## 1-last_digit.py

print the last digit of the number stored in the variable `number`.

## 2-print_alphabet.py

a program that prints the ASCII alphabet, in lowercase, not followed by a new line.

## 3-print_alphabt.py

a program that prints the ASCII alphabet, in lowercase, not followed by a new line.

## 4-print_hexa.py

a program that prints all numbers from `0` to `98` in decimal and in hexadecimal.

## 5-print_comb2.py

a program that prints numbers from 0 to 99.

## 6-print_comb3.py

a program that prints all possible different combinations of two digits.

## 7-islower.py

a function that checks for lowercase character.

- Prototype: `def islower(c):`
- Returns `True` if `c` is lowercase
- Returns `False` otherwise.

## 8-uppercase.py

a function that prints a string in uppercase followed by a new line.

- Prototype: `def uppercase(str):`

## 9-print_last_digit.py

a function that prints the last digit of a number.

- Prototype: `def print_last_digit(number):`
- Returns the value of the last digit.

## 10-add.py

a function that adds two integers and returns the result.

- Prototype: `def add(a, b):`
- Returns the value of `a + b`

## 11-pow.py

a function that computes a to the power of b and return the value.

- Prototype: `def pow(a, b):`
- Returns the value of `a ^ b`

## 12-fizzbuzz.py

a function that prints the numbers from `1` to `100` separated by a space.

- For multiples of three print `Fizz` instead of the number and for multiples of five print `Buzz`.
- For numbers which are multiples of both three and five print `FizzBuzz`.
- Prototype: `def fizzbuzz():`
- Each element should be followed by a space.

## 13-insert_number.c, lists.h

a function in `C` that inserts a number into a sorted singly linked list.

- Prototype: `listint_t *insert_node(listint_t **head, int number);`
- Return: the address of the new node, or `NULL` if it failed.

## 100-print_tebahpla.py

a program that prints the ASCII alphabet, in reverse order, alternating lowercase and uppercase (`z` in lowercase and `Y` in uppercase) , not followed by a new line.

## 101-remove_char_at.py

a function that creates a copy of the string, removing the character at the position `n` (not the Python way, the “`C` array index”).

- Prototype: `def remove_char_at(str, n):`

## 102-magic_calculation.py

a Python function `def magic_calculation(a, b, c):` that does exactly the same as the following Python bytecode:
```
  3           0 LOAD_FAST                0 (a)
              3 LOAD_FAST                1 (b)
              6 COMPARE_OP               0 (<)
              9 POP_JUMP_IF_FALSE       16

  4          12 LOAD_FAST                2 (c)
             15 RETURN_VALUE

  5     >>   16 LOAD_FAST                2 (c)
             19 LOAD_FAST                1 (b)
             22 COMPARE_OP               4 (>)
             25 POP_JUMP_IF_FALSE       36

  6          28 LOAD_FAST                0 (a)
             31 LOAD_FAST                1 (b)
             34 BINARY_ADD
             35 RETURN_VALUE

  7     >>   36 LOAD_FAST                0 (a)
             39 LOAD_FAST                1 (b)
             42 BINARY_MULTIPLY
             43 LOAD_FAST                2 (c)
             46 BINARY_SUBTRACT
             47 RETURN_VALUE
```
