# __0x07-python-test_driven_development__

## 0-add_integer.py

a function that adds 2 integers.

- Prototype: `def add_integer(a, b=98):`
- `a` and `b` must be integers or floats, otherwise raise a `TypeError` exception with the message `a must be an integer` or `b must be an integer`
- `a` and `b` will be first casted to integers if they are float
- Returns an integer: the addition of `a` and `b`

## 2-matrix_divided.py

a function that divides all elements of a matrix.

- Prototype: `def matrix_divided(matrix, div):`
- `matrix` must be a list of lists of integers or floats, otherwise raises a `TypeError` exception with the message `matrix must be a matrix (list of lists) of integers/floats`
- Each row of the `matrix` must be of the same size, otherwise raises a `TypeError` exception with the message `Each row of the matrix must have the same size`
- `div` must be a number (integer or float), otherwise raises a `TypeError` exception with the message `div must be a number`
- `div` can’t be equal to `0`, otherwise raises a `ZeroDivisionError` exception with the message `division by zero`
- All elements of the `matrix` will be divided by `div`, rounded to 2 decimal places
- Returns a new matrix

## 3-say_my_name.py

a function that prints `My name is <first name> <last name>`

- Prototype: `def say_my_name(first_name, last_name=""):`
- `first_name` and `last_name` must be strings otherwise, raises a `TypeError` exception with the message `first_name must be a string` or `last_name must be a string`

## 4-print_square.py

a function that prints a square with the character `#`.

- Prototype: `def print_square(size):`
- `size` is the size length of the square
- `size` must be an integer, otherwise raises a `TypeError` exception with the message `size must be an integer`
- if `size` is less than `0`, raises a `ValueError` exception with the message `size must be >= 0`
- if `size` is a float and is less than 0, raises a `TypeError` exception with the message `size must be an integer`

## 5-text_indentation.py

a function that prints a text with 2 new lines after each of these characters: `.`, `?` and `:`

- Prototype: `def text_indentation(text):`
- `text` must be a string, otherwise raises a `TypeError` exception with the message `text must be a string`

## tests/6-max_integer_test.py

unittests for the function `def max_integer(list=[]):`

```python
def max_integer(list=[]):
    """Function to find and return the max integer in a list of integers
        If the list is empty, the function returns None
    """
    if len(list) == 0:
        return None
    result = list[0]
    i = 1
    while i < len(list):
        if list[i] > result:
            result = list[i]
        i += 1
    return result
```

## 100-matrix_mul.py

a function that multiplies 2 matrices:

- Prototype: `def matrix_mul(m_a, m_b):`
- `m_a` and `m_b` must be validated with these requirements in this order
  - `m_a` and `m_b` must be an list of lists of integers or floats:
    - if `m_a` or `m_b` is not a list: raises a `TypeError` exception with the message `m_a must be a list` or `m_b must be a list`
    - if `m_a` or `m_b` is not a list of lists: raises a `TypeError` exception with the message `m_a must be a list of lists` or `m_b must be a list of lists`
    - if `m_a` or `m_b` is empty (it means:`= []` or `= [[]]`): raises a `ValueError` exception with the message `m_a can't be empty` or `m_b can't be empty`
    - if one element of those list of lists is not an integer or a float: raises a `TypeError` exception with the message `m_a should contain only integers or floats` or `m_b should contain only integers or floats`
    - if `m_a` or `m_b` is not a rectangle (all ‘rows’ should be of the same size): raises a `TypeError` exception with the message `each row of m_a must be of the same size` or `each row of m_b must be of the same size`
- If `m_a` and `m_b` can’t be multiplied: raises a `ValueError` exception with the message `m_a` and `m_b` can't be multiplied

## 101-lazy_matrix_mul.py

a function that multiplies 2 matrices by using the module `NumPy`

- Prototype: `def lazy_matrix_mul(m_a, m_b):`

## 102-python.c

a function that prints Python strings.

- Prototype: `void print_python_string(PyObject *p);`
- If `p` is not a valid string, prints an error message
