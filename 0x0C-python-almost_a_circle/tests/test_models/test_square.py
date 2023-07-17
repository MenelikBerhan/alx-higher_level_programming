#!/usr/bin/python3
"""Module containing `TestBase` class"""
import unittest
from contextlib import redirect_stdout
import io
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestSquare(unittest.TestCase):
    """Tests the Square class for various cases"""

    def setUp(self):
        """Create instances of Base class for testcases"""
        Base._Base__nb_objects = 0
        self.a = Square(1, 2)
        self.b = Square(2, 2, 3, 4)
        self.c = Square(3, 2, 3)
        self.d = Square(4)

    def tearDown(self):
        """Deletes objs created after each test"""
        del self.a, self.b, self.c, self.d

    def test_A_class(self):
        """Tests Square class type."""
        self.assertEqual(str(Square),
                         "<class 'models.square.Square'>")

    def test_B_inheritance(self):
        """Tests if Square inherits Rectangle."""
        self.assertTrue(issubclass(Square, (Rectangle, Base)))

    def test_init_(self):
        """Tests the __init__ method"""
        for obj in ([self.a, self.b, self.c, self.d]):
            self.assertEqual(str(type(obj)),
                             "<class 'models.square.Square'>")
            self.assertTrue(isinstance(obj, (Square, Rectangle, Base)))
        self.assertTrue(hasattr(Square, "__init__"))
        q = Square(1, 2, 3, "a")
        self.assertEqual(q.id, "a")
        with self.assertRaises(TypeError) as e:
            m = Square()
        with self.assertRaises(TypeError) as e:
            m = Square(1, 2, 3, 4, 5)
        try:
            m = Square('1', '2', '3', '4')
        except TypeError as e:
            self.assertIn("width must be an integer", e.args)
        try:
            m = Square(1, '2', '3', '4')
        except TypeError as e:
            self.assertIn("x must be an integer", e.args)
        try:
            m = Square(1, 2, '3', '4')
        except TypeError as e:
            self.assertIn("y must be an integer", e.args)
        try:
            m = Square(0, 1, 2, 3)
        except ValueError as e:
            self.assertIn("width must be > 0", e.args)
        try:
            m = Square(-1, 1, 2, 3)
        except ValueError as e:
            self.assertIn("width must be > 0", e.args)
        try:
            m = Square(1, -1, 2, 3)
        except ValueError as e:
            self.assertIn("x must be >= 0", e.args)
        try:
            m = Square(1, 2, -1, 3)
        except ValueError as e:
            self.assertIn("y must be >= 0", e.args)

    def test_id_attribute(self):
        """Test for id public instance attribute"""
        self.assertTrue(all(["id" in dir(x) for x in
                             [self.a, self.b, self.c]]))
        self.assertEqual(1, self.a.id)
        self.assertEqual(4, self.b.id)
        self.assertEqual(2, self.c.id)
        self.assertEqual(3, self.d.id)

    def test_nb_objects(self):
        "Test for nb_objects private class attribute"
        self.assertTrue("_Base__nb_objects" in dir(Square))
        self.assertTrue(all(["_Base__nb_objects" in dir(x) for x in
                             [self.a, self.b, self.c, self.d]]))
        with self.assertRaises(AttributeError) as e:
            Square.__nb_objects == 3

    def test_private_attributes(self):
        """Tests private attributes width, height, x and y"""
        self.assertTrue(all(["_Rectangle__width" in dir(x) for x in
                             [self.a, self.b, self.c, self.d]]))
        with self.assertRaises(AttributeError) as e:
            Square.__width == 3
        with self.assertRaises(AttributeError) as e:
            self.a.__width == 3
        self.assertTrue(all(["_Rectangle__height" in dir(x) for x in
                             [self.a, self.b, self.c, self.d]]))
        with self.assertRaises(AttributeError) as e:
            Square.__height == 3
        with self.assertRaises(AttributeError) as e:
            self.a.__height == 3
        self.assertTrue(all(["_Rectangle__x" in dir(x) for x in
                             [self.a, self.b, self.c, self.d]]))
        with self.assertRaises(AttributeError) as e:
            Square.__x == 3
        with self.assertRaises(AttributeError) as e:
            self.a.__x == 3
        self.assertTrue(all(["_Rectangle__y" in dir(x) for x in
                             [self.a, self.b, self.c, self.d]]))
        with self.assertRaises(AttributeError) as e:
            Square.__y == 3
        with self.assertRaises(AttributeError) as e:
            self.a.__y == 3

    def test_attributes_get(self):
        """Test for getters for width, height, x and y"""
        self.assertEqual(self.a.width, 1)
        self.assertEqual(self.a.height, 1)
        self.assertEqual(self.a.size, 1)
        self.assertEqual(self.a.x, 2)
        self.assertEqual(self.a.y, 0)
        self.assertEqual(self.b.width, 2)
        self.assertEqual(self.b.height, 2)
        self.assertEqual(self.b.size, 2)
        self.assertEqual(self.b.x, 2)
        self.assertEqual(self.b.y, 3)
        self.assertEqual(self.c.width, 3)
        self.assertEqual(self.c.height, 3)
        self.assertEqual(self.c.size, 3)
        self.assertEqual(self.c.x, 2)
        self.assertEqual(self.c.y, 3)
        self.assertEqual(self.d.width, 4)
        self.assertEqual(self.d.height, 4)
        self.assertEqual(self.d.size, 4)
        self.assertEqual(self.d.x, 0)
        self.assertEqual(self.d.y, 0)

    def test_attributes_set(self):
        """Test for setters for width, height, x and y"""
        try:
            self.a.width = '1'
        except TypeError as e:
            self.assertIn("width must be an integer", e.args)
        try:
            self.a.height = '1'
        except TypeError as e:
            self.assertIn("height must be an integer", e.args)
        try:
            self.a.size = '1'
        except TypeError as e:
            self.assertIn("width must be an integer", e.args)
        try:
            self.a.x = '1'
        except TypeError as e:
            self.assertIn("x must be an integer", e.args)
        try:
            self.a.y = '1'
        except TypeError as e:
            self.assertIn("y must be an integer", e.args)
        try:
            self.a.width = 0
        except ValueError as e:
            self.assertIn("width must be > 0", e.args)
        try:
            self.a.height = 0
        except ValueError as e:
            self.assertIn("height must be > 0", e.args)
        try:
            self.a.size = 0
        except ValueError as e:
            self.assertIn("width must be > 0", e.args)
        try:
            self.x = -1
        except ValueError as e:
            self.assertIn("x must be >= 0", e.args)
        try:
            self.y = -1
        except ValueError as e:
            self.assertIn("y must be >= 0", e.args)

    def test_area_method(self):
        """Tests the `area` public instance method"""
        self.assertTrue(all([hasattr(x, "area") for x in
                             [self.a, self.b, self.c, self.d]]))
        self.assertEqual(self.a.area(), 1)
        self.assertEqual(self.b.area(), 4)
        self.assertEqual(self.c.area(), 9)
        self.assertEqual(self.d.area(), 16)
        with self.assertRaises(TypeError) as e:
            m = self.a.area(1)
        with self.assertRaises(TypeError) as e:
            m = Square.area()

    def test_display_method(self):
        """Tests the `display` public instance method"""
        with self.assertRaises(TypeError) as e:
            m = self.a.display(23)
        with self.assertRaises(TypeError) as e:
            m = Square.display()
        self.assertTrue(all([hasattr(x, "display") for x in
                             [self.a, self.b, self.c, self.d]]))
        disp = io.StringIO()
        with redirect_stdout(disp):
            self.a.display()
        self.assertEqual(disp.getvalue(), "  #\n")
        disp = io.StringIO()
        with redirect_stdout(disp):
            self.b.display()
        self.assertEqual(disp.getvalue(), "\n\n\n  ##\n  ##\n")
        disp = io.StringIO()
        with redirect_stdout(disp):
            self.c.display()
        self.assertEqual(disp.getvalue(), "\n\n\n  ###\n  ###\n  ###\n")
        disp = io.StringIO()
        with redirect_stdout(disp):
            self.d.display()
        self.assertEqual(disp.getvalue(), "####\n####\n####\n####\n")

    def test_str_method(self):
        """Tests the `str` method"""
        with self.assertRaises(TypeError) as e:
            Square.__str__(self.a, 1)
        with self.assertRaises(TypeError) as e:
            Square.__str__()
        self.assertEqual(str(self.a), "[Square] (1) 2/0 - 1")
        self.assertEqual(str(self.b), "[Square] (4) 2/3 - 2")
        self.assertEqual(str(self.c), "[Square] (2) 2/3 - 3")
        self.assertEqual(str(self.d), "[Square] (3) 0/0 - 4")

    def test_update_method(self):
        """Tests the `update` instance method"""
        self.assertTrue(all([hasattr(x, "update") for x in
                             [self.a, self.b, self.c, self.d]]))
        with self.assertRaises(TypeError) as e:
            Square.update()
        self.a.update()
        self.assertEqual(str(self.a), "[Square] (1) 2/0 - 1")
        self.a.update(None)
        self.assertEqual(str(self.a), "[Square] (None) 2/0 - 1")
        self.a.update(11)
        self.assertEqual(str(self.a), "[Square] (11) 2/0 - 1")
        self.a.update(1, 2)
        self.assertEqual(str(self.a), "[Square] (1) 2/0 - 2")
        self.a.update(1, 2, 3)
        self.assertEqual(str(self.a), "[Square] (1) 3/0 - 2")
        self.a.update(1, 2, 3, 4)
        self.assertEqual(str(self.a), "[Square] (1) 3/4 - 2")
        with self.assertRaises(AttributeError) as e:
            self.a.update(1, 2, 3, 4, 5)
        self.a.update(**{'id': 11})
        self.assertEqual(str(self.a), "[Square] (11) 3/4 - 2")
        self.a.update(**{'id': 11, 'size': 5})
        self.assertEqual(str(self.a), "[Square] (11) 3/4 - 5")
        self.a.update(**{'id': 11, 'size': 5, 'x': 13})
        self.assertEqual(str(self.a), "[Square] (11) 13/4 - 5")
        self.a.update(**{'id': 11, 'size': 5, 'x': 13, 'y': 12})
        self.assertEqual(str(self.a), "[Square] (11) 13/12 - 5")
        with self.assertRaises(AttributeError) as e:
            self.a.update(**{'i': 11, 'sids': 5, 'xs': 3, 'ys': 2})
        self.a.update(9, **{'id': 8, 'size': 8, 'x': 8, 'y': 8})
        self.assertEqual(str(self.a), "[Square] (9) 13/12 - 5")

    def test_update_method_invalid_inputs_kwargs(self):
        """Tests the `update` instance method with invalid argument values"""
        try:
            self.a.update(**{'size': '5'})
        except TypeError as e:
            self.assertIn("width must be an integer", e.args)
        try:
            self.a.update(**{'x': '5'})
        except TypeError as e:
            self.assertIn("x must be an integer", e.args)
        try:
            self.a.update(**{'y': '5'})
        except TypeError as e:
            self.assertIn("y must be an integer", e.args)
        try:
            self.a.update(**{'size': 0})
        except ValueError as e:
            self.assertIn("width must be > 0", e.args)
        try:
            self.a.update(**{'x': -1})
        except ValueError as e:
            self.assertIn("x must be >= 0", e.args)
        try:
            self.a.update(**{'y': -1})
        except ValueError as e:
            self.assertIn("y must be >= 0", e.args)

    def test_update_method_invalid_inputs_args(self):
        """Tests the `update` instance method with invalid argument values"""
        try:
            self.a.update(1, '5')
        except TypeError as e:
            self.assertIn("width must be an integer", e.args)
        try:
            self.a.update(1, 2, '5')
        except TypeError as e:
            self.assertIn("x must be an integer", e.args)
        try:
            self.a.update(1, 2, 3, '5')
        except TypeError as e:
            self.assertIn("y must be an integer", e.args)
        try:
            self.a.update(1, -2, 3, 4)
        except ValueError as e:
            self.assertIn("width must be > 0", e.args)
        try:
            self.a.update(1, 2, -4, 5)
        except ValueError as e:
            self.assertIn("x must be >= 0", e.args)
        try:
            self.a.update(1, 2, 3, -5)
        except ValueError as e:
            self.assertIn("y must be >= 0", e.args)

    def test_to_dictionary_method(self):
        """Tests the `to_dictionary` public instance method"""
        with self.assertRaises(TypeError) as e:
            Square.to_dictionary()
        s = "to_dictionary() missing 1 required positional argument: 'self'"
        self.assertEqual(str(e.exception), s)

        d = {'x': 2, 'y': 0, 'size': 1, 'id': 1}
        self.assertEqual(self.a.to_dictionary(), d)
        d = {'x': 2, 'y': 3, 'size': 2, 'id': 4}
        self.assertEqual(self.b.to_dictionary(), d)
        d = {'x': 2, 'y': 3, 'size': 3, 'id': 2}
        self.assertEqual(self.c.to_dictionary(), d)
        d = {'x': 0, 'y': 0, 'size': 4, 'id': 3}
        self.assertEqual(self.d.to_dictionary(), d)

        self.a.x = 10
        self.a.y = 20
        self.a.size = 30
        d = {'x': 10, 'y': 20, 'size': 30, 'id': 1}
        self.assertEqual(self.a.to_dictionary(), d)

        a_dictionary = self.a.to_dictionary()
        self.b.update(**a_dictionary)
        self.assertEqual(str(self.a), str(self.b))
        self.assertNotEqual(self.a, self.b)


if __name__ == "__main__":
    unittest.main()
