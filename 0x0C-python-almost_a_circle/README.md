# __0x0C-python-almost_a_circle__

## __models.base.py__

A base class that defines an object with public attribute `id`

- private class attribute `__nb_objects = 0`
- class constructor: `def __init__(self, id=None):`:
  - if `id` is not `None`, assigns the public instance attribute `id` with this argument value - its assumed that `id` is an integer
  - otherwise, increments `__nb_objects` and assigns the new value to the public instance attribute `id`

- static method `def to_json_string(list_dictionaries):`
  - `list_dictionaries` is a list of dictionaries
    - If `list_dictionaries` is `None` or empty, returns the string: `"[]"`
    - Otherwise, returns the `JSON` string representation of `list_dictionaries`

- class method `def save_to_file(cls, list_objs):`
  - writes the `JSON` string representation of `list_objs` to a file:
  - `list_objs` is a list of instances who inherits of `Base` - example: list of `Rectangle` or list of `Square` instances
  - If `list_objs` is `None`, saves an empty list
  - The filename will be: `<Class name>.json` - example: `Rectangle.json`
  - Uses the static method `to_json_string` (mentioned before)
  - Overwrites the file if it already exists

- static method `def from_json_string(json_string):`
  - `json_string` is a string representing a list of dictionaries
  - If `json_string` is `None` or empty, returns an empty list
  - Otherwise, returns the list represented by `json_string`

- class method `def create(cls, **dictionary):`
  - returns an instance with all attributes already set:
  - `**dictionary` can be thought of as a double pointer to a dictionary
  - Uses the method `def update(self, *args, **kwargs)` and `**dictionary` is used as `**kwargs` of the method `update`
  - Does not use `eval`

- class method `def load_from_file(cls):`
  - The filename will be:`<Class name>.json` - example: `Rectangle.json`
  - If the file doesn’t exist, returns an empty list
  - Otherwise, returns a list of instances - the type of these instances depends on `cls` (current class using this method)
  - Uses the `from_json_string` and `create` methods (implemented previously)

- class methods `def save_to_file_csv(cls, list_objs):` and `def load_from_file_csv(cls):` that serializes and deserializes in `CSV`:
  - The filename will be: `<Class name>.csv` - example: `Rectangle.csv`
  - Has the same behavior as the `JSON` serialization/deserialization
  - Format of the `CSV`:
    - Rectangle: `<id>,<width>,<height>,<x>,<y>`
    - Square: `<id>,<size>,<x>,<y>`

- static method `def draw(list_rectangles, list_squares):` that opens a window and draws all the `Rectangles` and `Squares`:
  - Uses the `Turtle` graphics module

## __models.rectangle.py__

A class that defines a rectangle object by extending the `Base` class

- Private instance attributes, each with its own public getter and setter:
  - `__width` -> `width`
  - `__height` -> `height`
  - `__x` -> `x`
  - `__y` -> `y`

- Class constructor: `def __init__(self, width, height, x=0, y=0, id=None):`
  - Calls the super class with `id` - this super call will use the logic of the `__init__` of the Base class
  - Assigns each argument `width`, `height`, `x` and `y` to the right attribute

- validation of all setter methods and instantiation (`id` excluded):
  - If the input is not an integer, raises the `TypeError` exception with the message: `<name of the attribute> must be an integer`. Example: `width must be an integer`
  - If `width` or `height` is under or equals `0`, raises the `ValueError` exception with the message: `<name of the attribute> must be > 0`. Example: `width must be > 0`
  - If `x` or `y` is under `0`, raises the `ValueError` exception with the message: `<name of the attribute> must be >= 0`. Example: `x must be >= 0`

- public method `def area(self):` that returns the area value of the `Rectangle` instance.

- public method `def display(self):` that prints in `stdout` the `Rectangle` instance with the character `#` by taking care of `x` and `y`

- `__str__` method that it returns `[Rectangle] (<id>) <x>/<y> - <width>/<height>`

- public method `def update(self, *args, **kwargs):` that assigns an argument to each attribute:
  - for `*args:`
    - 1st argument should be the `id` attribute
    - 2nd argument should be the `width` attribute
    - 3rd argument should be the `height` attribute
    - 4th argument should be the `x` attribute
    - 5th argument should be the `y` attribute

  - `**kwargs` can be thought of as a double pointer to a dictionary: key/value
  - `**kwargs` will be skipped if `*args` exists and is not empty
  - Each key in this dictionary represents an attribute to the instance

## __models.square.py__

A class that defines a square object by extending the `Rectangle` class

- Class constructor: `def __init__(self, size, x=0, y=0, id=None):`
  - Calls the super class with `id`, `x`, `y`, `width` and `height` - this super call will use the logic of the `__init__` of the `Rectangle` class. The `width` and `height` will be assigned to the value of `size`
  - No new attributes are created for this class, uses all attributes of `Rectangle`
  - All `width`, `height`, `x` and `y` validation is inherited from `Rectangle` - same behavior in case of wrong data

- The overloading `__str__` method returns `[Square] (<id>) <x>/<y> - <size>`

- public getter and setter `size`
  - The setter assigns (in this order) the `width` and the `height` - with the same value
  - The setter have the same value validation as the `Rectangle` for `width` and `height`

- public method `def update(self, *args, **kwargs)` that assigns attributes:
  - `*args` is the list of arguments - no-keyworded arguments
    - 1st argument should be the `id` attribute
    - 2nd argument should be the `size` attribute
    - 3rd argument should be the `x` attribute
    - 4th argument should be the `y` attribute
  - `**kwargs` can be thought of as a double pointer to a dictionary: key/value (keyworded arguments)
  - `**kwargs` will be skipped if *args exists and is not empty
  - Each key in this dictionary represents an attribute to the instance

- public method `def to_dictionary(self):` that returns the dictionary representation of a Square:
  - This dictionary will contain:
    - `id`
    - `size`
    - `x`
    - `y`
