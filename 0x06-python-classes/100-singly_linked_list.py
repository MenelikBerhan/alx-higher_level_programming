#!/usr/bin/python3
"""A `Node` class that defines a node in a singly linked list and
a `SinglyLinkedList` class that defines a singly linked list of nodes."""


class Node():
    """Defies a node in a singly linked list with data and next node.

    Attributes:
        data (`int`): data of node
        next_node ('Node'): the node next to self
    """
    def __init__(self, data, next_node=None):
        """Initializes a `Node` object with data and next node

        Args:
            data (`int`): data of node
            next_node('Node`, optional): the node next to self

        Raises:
            TypeError: if data is not an integer or if next_node is not a Node
        """
        if type(data) != int:
            raise TypeError("data must be an integer")

        if next_node is not None and not isinstance(next_node, Node):
            raise TypeError("next_node must be a Node object")
        self.__data = data
        self.__next_node = next_node

    @property
    def data(self):
        """`int`: Getter and setter for `data` attribute of a Node\n
        For setter, Raises:
            TypeError: if data is not an integer
        """
        return self.__data

    @data.setter
    def data(self, value):
        if type(value) != int:
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """`Node`: Getter and setter for `next_node` attribute of a Node\n
        For setter, Raises:
            TypeError: if next_node is not a Node
        """
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        if value is not None and not isinstance(value, Node):
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList():
    """Defines a singlylinked list with a list of `Node` objectes

    Attributes:
        head (`list` of `Node`): a list of `Node` objects sorted by
            data attribute
    """
    def __init__(self):
        """Initializes a `Node` with an empty list"""
        self.__head = []

    def sorted_insert(self, value):
        """Inserts a new `Node` into the correct sorted position
            in the list (increasing order)\n
        Args:
            value (`Node`): node to be inserted into list
        """
        new_node = Node(value)
        self.__head.append(new_node)
        self.__head.sort(key=lambda node: node.data)
        i = 0
        for node in self.__head:
            if i < len(self.__head) - 1:
                node.next_node = self.__head[self.__head.index(node) + 1]
            i += 1

    def __str__(self):
        """`str`: a string representation of the singly linked list."""
        printable = ""
        len_list = len(self.__head)
        for i in range(len_list):
            end = "" if i == len_list - 1 else '\n'
            printable += str(self.__head[i].data) + end
        return printable
