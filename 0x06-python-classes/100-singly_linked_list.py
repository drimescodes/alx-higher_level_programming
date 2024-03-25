#!/usr/bin/python3
"""
Write a class `Node` that defines a node of a singly linked list by:
- Private instance attribute: `data`:
  - property `def data(self):` to retrieve it
  - property setter `def data(self, value):` to set it:
    - `data` must be an integer, otherwise raise a `TypeError` exception with
      the message `data must be an integer`
- Private instance attribute: `next_node`:
  - property `def next_node(self):` to retrieve it
  - property setter `def next_node(self, value):` to set it:
    - `next_node` can be `None` or must be a `Node`, otherwise raise a
      `TypeError` exception with the message `next_node must be a Node object`
- Instantiation with `data` and `next_node`:
  `def __init__(self, data, next_node=None):`
And, write a class `SinglyLinkedList` that defines a singly linked list by:
- Private instance attribute: `head` (no setter or getter)
- Simple instantiation: `def __init__(self):`
- Should be printable:
  - print the entire list in stdout
  - one node number by line
- Public instance method: `def sorted_insert(self, value):` that inserts a new
  `Node` into the correct sorted position in the list (increasing order)
- You are not allowed to import any module
"""


class Node:
    """The Node class"""

    def __init__(self, data, next_node=None):
        """Initialising the Node class"""
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """Retrieves the data"""
        return self.__data

    @data.setter
    def data(self, value):
        """Sets the data value"""
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """Retrieves the next_node"""
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """Sets the next_node value"""
        if not isinstance(value, Node) and value is not None:
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    """The SinglyLinkedList class"""

    def __init__(self):
        """Initialising the SinglyLinkedList class"""
        self.__head = None

    def __str__(self):
        """Returns the list as a string"""
        string = ""
        current = self.__head
        while current:
            string += str(current.data) + "\n"
            current = current.next_node
        return string[:-1]

    def sorted_insert(self, value):
        """Inserts a new Node into the correct sorted position in the list"""
        new = Node(value)
        if self.__head is None:
            self.__head = new
            return
        if self.__head.data > value:
            new.next_node = self.__head
            self.__head = new
            return
        current = self.__head
        while current.next_node and current.next_node.data < value:
            current = current.next_node
        new.next_node = current.next_node
        current.next_node = new
