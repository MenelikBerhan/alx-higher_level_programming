#!/usr/bin/python3
"""Module containing `TestBase` class"""
import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestBase(unittest.TestCase):
    """Tests the Base class for various cases"""

    def setUp(self):
        """Create instances of Base class for testcases"""
        Base._Base__nb_objects = 0
        self.a = Base()
        self.b = Base()
        self.c = Base(99)
        self.d = Base()

    def tearDown(self):
        """Deletes objs created after each test"""
        del self.a, self.b, self.c, self.d

    def test_init_(self):
        """Tests the __init__ method"""
        for obj in ([self.a, self.b, self.c, self.d]):
            self.assertEqual(str(type(obj)), "<class 'models.base.Base'>")
            self.assertTrue(isinstance(obj, Base))
        self.assertTrue(hasattr(Base, "__init__"))
        with self.assertRaises(TypeError) as e:
            m = Base(1, 2)

    def test_id_attribute(self):
        """Test for id public instance attribute"""
        self.assertTrue(all(["id" in dir(x) for x in
                             [self.a, self.b, self.c, self.d]]))
        self.assertEqual(1, self.a.id)
        self.assertEqual(2, self.b.id)
        self.assertEqual(99, self.c.id)
        self.assertEqual(3, self.d.id)
        e = Base("a")
        self.assertEqual(e.id, "a")

    def test_nb_objects(self):
        """Test for nb_objects private class attribute"""
        self.assertTrue("_Base__nb_objects" in dir(Base))
        self.assertTrue(all(["_Base__nb_objects" in dir(x) for x in
                             [self.a, self.b, self.c, self.d]]))
        with self.assertRaises(AttributeError) as e:
            Base.__nb_objects == 3
        self.assertEqual(getattr(Base, "_Base__nb_objects"), self.d.id)

    def test_to_json_string(self):
        """Tests `to_json_string` signature:"""
        with self.assertRaises(TypeError) as e:
            Base.to_json_string()

        self.assertEqual(Base.to_json_string(None), "[]")
        self.assertEqual(Base.to_json_string([]), "[]")
        d = [{'x': 101, 'y': 123, 'width': 321, 'id': 529, 'height': 440}]
        self.assertEqual(len(Base.to_json_string(d)), len(str(d)))
        d = [{'x': 1, 'y': 2, 'width': 3, 'id': 4, 'height': 5}]
        self.assertEqual(len(Base.to_json_string(d)), len(str(d)))
        d = [{"g": 77}]
        self.assertEqual(Base.to_json_string(d), '[{"g": 77}]')
        d = [{"g": 77}, {"ghi": 123}, {"GH": 0}]
        self.assertEqual(Base.to_json_string(d),
                         '[{"g": 77}, {"ghi": 123}, {"GH": 0}]')

        d = [{'x': 1, 'y': 2, 'width': 3, 'id': 4, 'height': 5},
             {'x': 101, 'y': 23, 'width': 21, 'id': 54, 'height': 34}]
        self.assertEqual(len(Base.to_json_string(d)),
                         len(str(d)))
        d = [{}]
        self.assertEqual(Base.to_json_string(d), '[{}]')
        d = [{}, {}]
        self.assertEqual(Base.to_json_string(d), '[{}, {}]')

        r1 = Rectangle(20, 13, 12, 80)
        dictionary = r1.to_dictionary()
        json_dictionary = Base.to_json_string([dictionary])
        dictionary = str([dictionary])
        dictionary = dictionary.replace("'", '"')
        self.assertEqual(dictionary, json_dictionary)

        r1 = Rectangle(4, 5, 6, 7)
        r2 = Rectangle(8, 9, 10, 11)
        r3 = Rectangle(12, 13, 14, 15)
        dictionary = [r1.to_dictionary(), r2.to_dictionary(),
                      r3.to_dictionary()]
        json_dictionary = Base.to_json_string(dictionary)
        dictionary = str(dictionary)
        dictionary = dictionary.replace("'", '"')
        self.assertEqual(dictionary, json_dictionary)

        r1 = Square(1, 2, 3)
        dictionary = r1.to_dictionary()
        json_dictionary = Base.to_json_string([dictionary])
        dictionary = str([dictionary])
        dictionary = dictionary.replace("'", '"')
        self.assertEqual(dictionary, json_dictionary)

        r1 = Square(1, 2, 3)
        r2 = Square(4, 5, 6)
        r3 = Square(7, 8, 9)
        dictionary = [r1.to_dictionary(), r2.to_dictionary(),
                      r3.to_dictionary()]
        json_dictionary = Base.to_json_string(dictionary)
        dictionary = str(dictionary)
        dictionary = dictionary.replace("'", '"')
        self.assertEqual(dictionary, json_dictionary)

    def test_save_to_file(self):
        """Tests `save_to_file` method."""
        import os
        r1 = Rectangle(1, 2, 3, 4)
        r2 = Rectangle(5, 6)
        list_objs = [r1.to_dictionary(), r2.to_dictionary()]
        json_str = Base.to_json_string(list_objs)
        Rectangle.save_to_file([r1, r2])
        with open("Rectangle.json", "r") as file:
            self.assertEqual(len(file.read()), len(json_str))
        Rectangle.save_to_file(None)
        with open("Rectangle.json", "r") as file:
            self.assertEqual(file.read(), "[]")
        try:
            os.remove("Rectangle.json")
        except Exception as e:
            pass
        Rectangle.save_to_file([])
        with open("Rectangle.json", "r") as file:
            self.assertEqual(file.read(), "[]")
        r2 = Rectangle(1, 2)
        list_objs = [r2.to_dictionary()]
        json_str = Base.to_json_string(list_objs)
        Rectangle.save_to_file([r2])
        with open("Rectangle.json", "r") as file:
            self.assertEqual(len(file.read()), len(json_str))

        Square.save_to_file(None)
        with open("Square.json", "r") as file:
            self.assertEqual(file.read(), "[]")
        try:
            os.remove("Square.json")
        except Exception as e:
            pass
        Square.save_to_file([])
        with open("Square.json", "r") as file:
            self.assertEqual(file.read(), "[]")
        r2 = Square(23)
        list_objs = [r2.to_dictionary()]
        json_str = Base.to_json_string(list_objs)
        Square.save_to_file([r2])
        with open("Square.json", "r") as file:
            self.assertEqual(len(file.read()), len(json_str))

    def test_create(self):
        """Tests `create` method."""
        r1 = Rectangle(8, 9, 10)
        r1_dictionary = r1.to_dictionary()
        r2 = Rectangle.create(**r1_dictionary)
        self.assertEqual(str(r1), str(r2))
        self.assertFalse(r1 is r2)
        self.assertFalse(r1 == r2)

    def test_load_from_file(self):
        """Tests `load_from_file` method."""
        r1 = Rectangle(10, 13, 21, 18)
        r2 = Rectangle(13, 42)
        list_in = [r1, r2]
        Rectangle.save_to_file(list_in)
        list_out = Rectangle.load_from_file()
        self.assertNotEqual(id(list_in[0]), id(list_out[0]))
        self.assertEqual(str(list_in[0]), str(list_out[0]))
        self.assertNotEqual(id(list_in[1]), id(list_out[1]))
        self.assertEqual(str(list_in[1]), str(list_out[1]))

        s1 = Square(8)
        s2 = Square(12, 13, 14)
        list_in = [s1, s2]
        Square.save_to_file(list_in)
        list_out = Square.load_from_file()
        self.assertNotEqual(id(list_in[0]), id(list_out[0]))
        self.assertEqual(str(list_in[0]), str(list_out[0]))
        self.assertNotEqual(id(list_in[1]), id(list_out[1]))
        self.assertEqual(str(list_in[1]), str(list_out[1]))


if __name__ == "__main__":
    unittest.main()
