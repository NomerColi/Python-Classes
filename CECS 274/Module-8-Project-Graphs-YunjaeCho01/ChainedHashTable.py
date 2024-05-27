from Interfaces import Set
from DLList import DLList
import numpy as np


class ChainedHashTable(Set):

    class Node:

        def __init__(self, key, value):
            self.key = key
            self.value = value

    def __init__(self, listType=DLList):
        """
        initializes an empty table so that each bin holds a list
        of the given type
        :param listType: object type; the data type of the List;
                      defaults to DLList if dtype is not specified
        """
        self.lstType = listType
        self.d = 1
        self.t = self._alloc_table(2**self.d)
        self.z = 193759204821
        self.w = 31
        self.n = 0

    def _alloc_table(self, n: int):
        """
        helper method; creates a table with a given
        number of bins and given list type
        :param n: int type; the number of bins in the table
        """
        t = np.zeros(n, dtype=object)
        for i in range(n):
            t[i] = self.lstType()
        return t

    def _hash(self, key: object) -> int:
        """
        helper method; computes the hash value (i.e. bin number) for the given key
        """
        return self.z * hash(key) % (2**self.w) >> (self.w - self.d)

    def find(self, key: object) -> object:
        """
        finds the value corresponding to the given key
        :param key: object type; the key of the item to search for
        :returns: object type; the value corresponding to the key, if the key exists
                  otherwise, returns None
        """
        bin = self._hash(key)
        for i in self.t[bin]:
            if i.key == key:
                return i.value
        return None

    def add(self, key: object, value: object):
        """
        adds the given key-value pair to the table, if the key does not already exist
        in the table. 
        :param key: object type; the key of the item to add
        :param value: object type; the value of the item to add
        :returns: True if the value was successfully added; False if key already exists and 
                  new item was not added
        """
        if self.find(key) != None:
            return False
        if self.n == len(self.t):
            self.resize()
        bin = self._hash(key)
        item = self.Node(key, value)
        self.t[bin].append(item)
        self.n += 1
        return True

    def remove(self, key: int) -> object:
        """
        if the key exists, removes the item with the given key and returns its value;
        otherwise returns None
        :param key: object type; the key of the item to remove
        :returns: object type or None type;
        """
        idx = 0
        bin = self._hash(key)
        for i in self.t[bin]:
            if i.key == key:
                v = self.t[bin].remove(idx)
                self.n -= 1
                if len(self.t) >= self.n * 3:
                    self.resize()
                return v
            idx += 1
        return None

    def resize(self):
        """
        resizes the table to double the number of bins if the current number of
        bins is the same as the number of elements; otherwise resizes to half the
        number of bins
        """

        if self.n == len(self.t):
            self.d += 1
        else:
            self.d -= 1

        size = 2**self.d
        temp = np.zeros(size, dtype=object)
        for i in range(size):
            temp[i] = self.lstType()

        for l in self.t:
            for i in l:
                bin = self._hash(i.key)
                temp[bin].append(i)

        self.t = temp

    def size(self) -> int:
        """
        returns the number of items in the table
        :returns: int type;
        """
        return self.n

    def set(self, key, new_value):
        """
        replaces the value of the given key
        :param key: object type; the key of the item to modify
        :param new_value: object type; the
        :return: object type; the old value corresponding to key that was replaced
        :raises: ValueError if the given key does not exist in the table
        """
        bin = self._hash(key)
        for i in self.t[bin]:
            if i.key == key:
                old_value = i.value
                i.value = new_value
                return old_value

        return None

    def get_keys(self):
        """
        returns a list of all keys stored in the table
        :returns: Python list object
        """
        list = []
        for l in self.t:
            for i in l:
                list.append(i.key)
        return list

    def __str__(self):
        """
        returns a string representation of the table with key-value items
        in format (key, value)
        :returns: str type;
        """
        s = "\n"
        for i in range(len(self.t)):
            s += str(i) + " : "
            for j in range(len(self.t[i])):
                k = self.t[i][j]  # jth node at ith list
                s += "(" + str(k.key) + ", " + str(k.value) + "); "

            s += "\n"
        return s
