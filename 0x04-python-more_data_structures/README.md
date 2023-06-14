# 0x04-python-more_data_structures

## 0-square_matrix_simple.py

a function that computes the square value of all integers of a matrix

- Prototype: `def square_matrix_simple(matrix=[]):`
- `matrix` is a `2` dimensional array
- Returns a new matrix:
  - Same size as `matrix`
  - Each value is the square of the value of the input
- Initial matrix will not be modified

## 1-search_replace.py

a function that replaces all occurrences of an element by another in a new list.

- Prototype: `def search_replace(my_list, search, replace):`
- `my_list` is the initial list
- `search` is the element to replace in the list
- `replace` is the new element

## 2-uniq_add.py

 a function that adds all unique integers in a list (only once for each integer).

- Prototype: `def uniq_add(my_list=[]):`

## 3-common_elements.py

a function that returns a set of common elements in two sets.

- Prototype: `def common_elements(set_1, set_2):`

## 4-only_diff_elements.py

a function that returns a set of all elements present in only one set.

- Prototype: `def only_diff_elements(set_1, set_2):`

## 5-number_keys.py

a function that returns the number of keys in a dictionary.

- Prototype: `def number_keys(a_dictionary):`

## 6-print_sorted_dictionary.py

a function that prints a dictionary by ordered keys.

- Prototype: `def print_sorted_dictionary(a_dictionary):`
- It's assumed that all keys are strings but values can have any type
- Keys will be sorted by alphabetic order and keys of a dictionary inside the main dictionary will not be sorted

## 7-update_dictionary.py

a function that replaces or adds key/value in a dictionary.

- Prototype: `def update_dictionary(a_dictionary, key, value):`
- `key` argument will be always a string and `value` argument will be any type
- If a `key` exists in the dictionary, the value will be replaced
- If a `key` doesn’t exist in the dictionary, it will be created

## 8-simple_delete.py

a function that deletes a key in a dictionary.

- Prototype: `def simple_delete(a_dictionary, key=""):`
- `key` argument will be always a string
- If a `key` doesn’t exist, the dictionary won’t change

## 9-multiply_by_2.py

a function that returns a new dictionary with all values multiplied by 2

- Prototype: `def multiply_by_2(a_dictionary):`
- It's assumed that all values are only integers
- Returns a new dictionary

## 10-best_score.py

a function that returns a key with the biggest integer value.

- Prototype: `def best_score(a_dictionary):`
- It's assumed that all values are only integers and ll students have a different score
- If no score found, returns `None`

## 11-multiply_list_map.py

a function that returns a list with all values multiplied by a number without using any loops.

- Prototype: `def multiply_list_map(my_list=[], number=0):`
- Returns a new list:
  - Same length as `my_list`
  - Each value will be multiplied by `number`
- Initial list will not be modified

## 12-roman_to_int.py

a function that converts a Roman numeral to an integer.

- Prototype: `def roman_to_int(roman_string)`
- number will be between 1 to 3999.
- Return: an integer
- If the `roman_string` is not a string or `None`, returns `0`

## 100-weight_average.py

a function that returns the weighted average of all integers tuple (<`score`>, <`weight`>)

- Prototype: `def weight_average(my_list=[]):`
- Returns `0` if the list is empty

## 101-square_matrix_map.py

a function that computes the square value of all integers of a matrix using `map`

- Prototype: `def square_matrix_map(matrix=[]):`
- `matrix` is a 2 dimensional array
- Returns a new matrix:
  - Same size as `matrix`
  - Each value will be the square of the value of the input
- Initial matrix will not be modified

## 102-complex_delete.py

a function that deletes keys with a specific value in a dictionary.

- Prototype: `def complex_delete(a_dictionary, value):`
- If the `value` doesn’t exist, the dictionary won’t change
- All keys having the searched value have to be deleted

## 103-python.c

two `C` functions that print some basic info about Python lists and Python bytes objects.

1. Python lists:

	- Prototype: `void print_python_list(PyObject *p);`

2. Python bytes:

	- Prototype: `void print_python_bytes(PyObject *p);`
