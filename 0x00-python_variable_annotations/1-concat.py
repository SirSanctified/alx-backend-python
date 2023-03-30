#!/usr/bin/python3

"""
Contains a type-annotated function concat that takes a string str1
and a string str2 as arguments and returns a concatenated string
"""


def concat(str1: str, str2: str) -> str:
    """
    takes a string str1 and a string str2 as arguments
    and returns a concatenated string
    """
    return str1 + str2


if __name__ == '__main__':
    str1 = "egg"
    str2 = "shell"

    print(concat(str1, str2) == "{}{}".format(str1, str2))
    print(concat.__annotations__)
