#!/usr/bin/python3
"""Module containing `Base` class"""
import json
import csv


class Base:
    """Base class for classes in this project. Defines
    a basic object with id."""

    __nb_objects = 0

    def __init__(self, id=None):
        """Initializes a `Base class instance"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = self.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """`str`: Returns a `JSON` string representation of
        list of dictionaries"""
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """Writes the `JSON` string representation of `list_objs` to a file
        named `<Class name>.json`."""
        # check if objs in list are of the same class and of class `cls`
        file_name = cls.__name__ + ".json"
        if list_objs is None:
            with open(file_name, "w", encoding="utf-8") as file:
                file.write(Base.to_json_string(None))
        else:
            list_dicts = []
            for obj in list_objs:
                list_dicts.append(obj.to_dictionary())
            with open(file_name, "w", encoding="utf-8") as file:
                file.write(Base.to_json_string(list_dicts))

    @staticmethod
    def from_json_string(json_string):
        """`list`: Returns the list of objects represented by the
        `JSON` string representation `json_string`"""
        if json_string is None or len(json_string) == 0:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """`cls`: Returns an instance of `cls` with attributes set
        from key word arguments in `dictionary`"""
        if dictionary is None:  # checks: if mandatory attrs, valid attrs?
            return None
        # if cls.__name__ == "Rectangle":
        #     new_obj = cls(1, 1)
        # elif cls.__name__ == "Square":
        #     new_obj = cls(1)
        new_obj = cls(1, 1)
        new_obj.update(**dictionary)
        return new_obj

    @classmethod
    def load_from_file(cls):
        """`list`: Returns list of instances of `cls` from a file.
        The file name must be either `Rectangle.json` or `Square.json`"""
        try:
            with open((cls.__name__ + ".json"), encoding="utf-8") as file:
                list_dicts = cls.from_json_string(file.read())
        except FileNotFoundError:
            return []
        else:
            list_objs = []
            for dict_ in list_dicts:  # check for valid dict_?
                list_objs.append(cls.create(**dict_))
            return list_objs

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """Writes the `CSV` string representation of `list_objs` to a file
        named `<Class name>.csv`."""
        # check if objs in list are of the same class and of class `cls`?
        file_name = cls.__name__ + ".csv"
        if list_objs is None:
            with open(file_name, "w", encoding="utf-8") as file:
                file.write("")
        else:
            list_vals = []
            for obj in list_objs:
                list_vals.append(obj.to_dictionary().values())
            with open(file_name, "w", encoding="utf-8") as file:
                write_file = csv.writer(file)
                write_file.writerows(list_vals)

    @classmethod
    def load_from_file_csv(cls):
        """`list`: Returns list of instances of `cls` from a file.
        The file name must be either `Rectangle.csv` or `Square.csv`"""
        try:
            with open((cls.__name__ + ".csv"), encoding="utf-8") as file:
                list_vals = list(csv.reader(file))
        except FileNotFoundError:
            return []
        else:
            list_objs = []
            for row in list_vals:  # check for valid values?
                obj = cls(1, 1)
                obj.update(*list(map(int, row)))
                list_objs.append(obj)
            return list_objs
