#!/usr/bin/python3
"""defines an inherited list class MyList"""


class MyList(list):
    """does sorted printing for the built-in list class"""

    def print_sorted(self):
        """print a list sorted in ascending order"""
        print(sorted(self))
