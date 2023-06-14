# __0x03-python-data_structures__

## 0-print_list_integer.py

a function that prints all integers of a list.

- Prototype: `def print_list_integer(my_list=[]):`
- It is assumed that the list only contains integers.

## 1-element_at.py

a function that retrives an element from a list like in `C`.

- Prototype: `def element_at(my_list, idx):`
- The function returns `None` if `idx` is negative or is out of range (> of number of element in `my_list`).

## 2-replace_in_list.py

a function that replaces an element of a list at a specific position (like in `C`).

- Prototype: `def replace_in_list(my_list, idx, element):`
- If `idx` is negative or is out of range (> of number of element in `my_list`), the function does not modify anything, and returns the original list.

## 3-print_reversed_list_integer.py

a function that prints all integers of a list, in reverse order.

- Prototype: `def print_reversed_list_integer(my_list=[]):`

## 4-new_in_list.py

a function that replaces an element in a list at a specific position without modifying the original list (like in `C`).

- Prototype: `def new_in_list(my_list, idx, element):`
- If `idx` is negative or is out of range (> of number of element in `my_list`) the function should return a copy of the original list.

## 5-no_c.py

a function that removes all characters `c` and `C` from a string.

- Prototype: `def no_c(my_string):`
- The function returns the new string.

## 6-print_matrix_integer.py

a function that prints a matrix of integers.

- Prototype: `def print_matrix_integer(matrix=[[]]):`

## 7-add_tuple.py

a  function that adds 2 tuples.

- Prototype: `def add_tuple(tuple_a=(), tuple_b=()):`
- Returns a tuple with 2 integers:
    - The addition of the first element of each argument as the first element
    - The addition of the second element of each argument as the second element
- It is assumed that the list only contains integers.
- If a tuple is smaller than 2, value of `0` is used for each missing integer and if a tuple is bigger than 2, only the first 2 integers will be used.

## 8-multiple_returns.py

a function that returns a tuple with the length of a string and its first character.

- Prototype: `def multiple_returns(sentence):`
- If the sentence is empty, the first character will be equal to `None`

## 9-max_integer.py

a function that finds the biggest integer of a list.

- Prototype: `def max_integer(my_list=[]):`
- If the list is empty, returns `None`
- It is assumed that the list only contains integers.

## 10-divisible_by_2.py

a function that finds all multiples of 2 in a list.

- Prototype: `def divisible_by_2(my_list=[]):`
- Returns a new list with `True` or `False`, depending on whether the integer at the same position in the original list is a multiple of 2
- The new list will have the same size as the original list.

## 11-delete_at.py

a function that deletes the item at a specific position in a list.

- Prototype: `def delete_at(my_list=[], idx=0):`
- If `idx` is negative or out of range, nothing change (returns the same list)

## 12-switch.py

switches values stored in variable `a` and `b`.

## 13-is_palindrome.c

a `C` function that checks if a singly linked list is a palindrome.

- Prototype: `int is_palindrome(listint_t **head);`
- Return: `0` if it is not a palindrome, `1` if it is a palindrome
- An empty list is considered a palindrome.

## 100-print_python_list_info.c

a `C` function that prints some basic info about Python lists.

- Prototype: `void print_python_list_info(PyObject *p);`
