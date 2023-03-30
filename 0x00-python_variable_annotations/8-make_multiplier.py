#!/usr/bin/python3

"""
Contains a type-annotated function make_multiplier that takes
a float multiplier as argument
and returns a function that multiplies a float by multiplier.
"""

from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    Returns a callable 'inner'
    """
    def inner(multiplier: float) -> float:
        """Returns a float multiplied by itself"""
        return multiplier * multiplier
    return inner


if __name__ == '__main__':
    print(make_multiplier.__annotations__)
    fun = make_multiplier(2.22)
    print("{}".format(fun(2.22)))
