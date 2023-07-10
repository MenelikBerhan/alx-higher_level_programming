# __0x0A-python-inheritance__

## 0-looup.py

a function that returns the list of available attributes and methods of an object:

- Prototype: `def lookup(obj):`
- Returns a `list` object

## 1-my_list.py

a class `MyList` that inherits from `list`:

- Public instance method: `def print_sorted(self):` that prints the list, but sorted (ascending sort)
- It's assumed that all the elements of the list will be of type `int`

## 2-is_same_class.py

a function that returns `True` if the object is _exactly_ an instance of the specified class ; otherwise `False`.

- Prototype: `def is_same_class(obj, a_class):`

## 3-is_kind_of_class.py

a function that returns `True` if the object is an instance of, or if the object is an instance of a class that inherited from, the specified class ; otherwise `False`.

- Prototype: `def is_kind_of_class(obj, a_class):`

## 4-inherits_from.py

a function that returns `True` if the object is an instance of a class that inherited (directly or indirectly) from the specified class ; otherwise `False`.

- Prototype: `def inherits_from(obj, a_class):`

## 5-base_geometry.py

an empty class `BaseGeometry`.

## 6-base_geometry.py

a class `BaseGeometry` (based on `5-base_geometry.py`).

- Public instance method: `def area(self):` that raises an `Exception` with the message `area() is not implemented`

## 7-base_geometry.py

a class `BaseGeometry` (based on `6-base_geometry.py`).

- Public instance method: `def area(self):` that raises an `Exception` with the message `area() is not implemented`
- Public instance method: `def integer_validator(self, name, value):` that validates `value`:
  - it's assumed that `name` is always a string
  - if `value` is not an integer: raise a `TypeError` exception, with the message `<name> must be an integer`
  - if `value` is less or equal to `0`: raise a `ValueError` exception with the message `<name> must be greater than 0`

## 8-rectangle.py

a class `Rectangle` that inherits from `BaseGeometry` (`7-base_geometry.py`).

- Instantiation with `width` and `height`: `def __init__(self, width, height):`
  - `width` and `height` are private. No getter or setter
  - `width` and `height` must be positive integers, validated by `integer_validator`

## 9-rectangle.py

a class `Rectangle` that inherits from `BaseGeometry` (`7-base_geometry.py`). (task based on `8-rectangle.py`)

- Instantiation with `width` and `height`: `def __init__(self, width, height):`
  - `width` and `height` are private. No getter or setter
  - `width` and `height` must be positive integers, validated by `integer_validator`
- the `area()` method is implemented
- `print()` prints, and str() returns, the following rectangle description: `[Rectangle] <width>/<height>`

## 10-square.py

a class `Square` that inherits from `Rectangle` (`9-rectangle.py`):

- Instantiation with `size`: `def __init__(self, size):`:
  - `size` is private. No getter or setter
  - `size` must be a positive integer, validated by `integer_validator`
- the `area()` method is implemented

## 11-square.py

a class `Square` that inherits from `Rectangle` (`9-rectangle.py`). (task based on `10-square.py`).

- Instantiation with `size`: `def __init__(self, size):`:
  - `size` is private. No getter or setter
  - `size` must be a positive integer, validated by `integer_validator`
- the `area()` method is implemented
- `print()` prints, and `str()` returns, the square description: `[Square] <width>/<height>`

## 100-my_int.py

a class `MyInt` that inherits from `int`:

- `MyInt` is a rebel. `MyInt` has `==` and `!=` operators inverted

## 101-add_attribute.py

a function that adds a new attribute to an object if it’s possible:

- Raise a `TypeError` exception, with the message `can't add new attribute` if the object can’t have new attribute
- `try/except` is not used
