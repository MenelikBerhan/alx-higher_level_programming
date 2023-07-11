# __0x0B-python-input_output__

## 0-read_file.py

a function that reads a text file (`UTF8`) and prints it to `stdout`:

- Prototype: `def read_file(filename=""):`
- Uses the `with` statement and doesn't manage `file permission` or `file doesn't exist` exceptions.

## 1-write_file.py

a function that writes a string to a text file (`UTF8`) and returns the number of characters written:

- Prototype: `def write_file(filename="", text=""):`
- Uses the `with` statement and doesn't manage `file permission` exceptions.
- Creates the file if it doesn’t exist, and overwrites the content of the file if it already exists.

## 2-append_write.py

a function that appends a string at the end of a text file (`UTF8`) and returns the number of characters added:

- Prototype: `def append_write(filename="", text=""):`
- Creates the file if it doesn’t exist
- You must use the with statement
- Uses the `with` statement and doesn't manage `file permission` or `file doesn't exist` exceptions.

## 3-to_json_string.py

a function that returns the `JSON` representation of an object (string):

- Prototype: `def to_json_string(my_obj):`
- Doesn’t manage exceptions if the object can’t be serialized.

## 4-from_json_string.py

a function that returns an object (Python data structure) represented by a `JSON` string:

- Prototype: `def from_json_string(my_str):`
- Doesn’t manage exceptions if the `JSON` string doesn’t represent an object.

## 5-save_to_json_file.py

a function that writes an Object to a text file, using a `JSON` representation:

- Prototype: `def save_to_json_file(my_obj, filename):`
- Uses the `with` statement and doesn't manage exceptions if the object can’t be serialized or `file permission` exceptions.

## 6-load_from_json_file.py

a function that creates an Object from a `JSON` file:

- Prototype: `def load_from_json_file(filename):`
- Uses the `with` statement and doesn’t manage exceptions if the `JSON` string doesn’t represent an object.
- Doesn’t manage `file permissions` exceptions.

## 7-add_item.py

a script that adds all arguments to a Python list, and then save them to a file:

- Uses function `save_to_json_file` from `5-save_to_json_file.py` and function `load_from_json_file` from `6-load_from_json_file.py`
- The list will be saved as a `JSON` representation in a file named `add_item.json`
- If the file doesn’t exist, it will be created
- Doesn’t manage `file permissions` exceptions.

## 8-class_to_json.py

a function that returns the dictionary description with simple data structure (list, dictionary, string, integer and boolean) for `JSON` serialization of an object:

- Prototype: `def class_to_json(obj):`
- `obj` is an instance of a Class
- All attributes of the `obj` Class are assumed to be serializable: list, dictionary, string, integer and boolean.

## 9-student.py

a class `Student` that defines a student by:

- Public instance attributes:
  - `first_name`
  - `last_name`
  - `age`
- Instantiation with `first_name`, `last_name` and `age`: `def __init__(self, first_name, last_name, age):`
- Public method `def to_json(self):` that retrieves a dictionary representation of a `Student` instance (same as `8-class_to_json.py`)

## 10-student.py

a class `Student` that defines a student by:

- Public instance attributes:
  - `first_name`
  - `last_name`
  - `age`
- Instantiation with `first_name`, `last_name` and `age`: `def __init__(self, first_name, last_name, age):`
- Public method `def to_json(self):` that retrieves a dictionary representation of a `Student` instance (same as `8-class_to_json.py`)
  - If `attrs` is a list of strings, only attribute names contained in this list will be retrieved.
  - Otherwise, all attributes will be retrieved.

## 11-student.py

a class `Student` that defines a student by:

- Public instance attributes:
  - `first_name`
  - `last_name`
  - `age`
- Instantiation with `first_name`, `last_name` and `age`: `def __init__(self, first_name, last_name, age):`
- Public method `def to_json(self):` that retrieves a dictionary representation of a `Student` instance (same as `8-class_to_json.py`)
  - If `attrs` is a list of strings, only attribute names contained in this list will be retrieved.
  - Otherwise, all attributes will be retrieved.
- Public method `def reload_from_json(self, json):` that replaces all attributes of the `Student` instance:
  - It's assumed that `json` will always be a dictionary
  - A dictionary key will be the public attribute name
  - A dictionary value will be the value of the public attribute.

## 12-pascal_triangle.py

a function `def pascal_triangle(n):` that returns a list of lists of integers representing the Pascal’s triangle of `n`:

- Returns an empty list if `n <= 0`
- It's assumed that `n` will be always an integer.

## 100-append_after.py

a function that inserts a line of text to a file, after each line containing a specific string:

- Prototype: `def append_after(filename="", search_string="", new_string=""):`
- Uses the `with` statement and doesn’t need to manage `file permission` or f`ile doesn't exist` exceptions.

## 101-stats.py

 a script that reads `stdin` line by line and computes metrics:

- Input format: `<IP Address> - [<date>] "GET /projects/260 HTTP/1.1" <status code> <file size>`
- Each 10 lines and after a keyboard interruption (`CTRL + C`), prints those statistics since the beginning:
  - Total file size: `File size: <total size>`
  - where is the sum of all previous (see input format above)
  - Number of lines by status code:
    - possible status code: `200`, `301`, `400`, `401`, `403`, `404`, `405` and `500`
    - if a status code doesn’t appear, doesn’t print anything for this status code
    - format: `<status code>: <number>`
    - status codes will be printed in ascending order.
