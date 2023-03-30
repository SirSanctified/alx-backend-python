#!/usr/bin/env python3

"""
Contains a type-annotated function to_kv that takes a string k
and an int OR float v as arguments and returns a tuple.
The first element of the tuple is the string k.
The second element is the square of the int/float v
and should be annotated as a float.
"""

from typing import Tuple, Union


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """Use complex type annotations

    Args:
        k (str): a string argument
        v (Union[int, float]): an int or a float

    Returns:
        Tuple[str, float]: the second element is the square of v
    """
    return (k, v**2)


if __name__ == '__main__':
    print(to_kv.__annotations__)
    print(to_kv("eggs", 3))
    print(to_kv("school", 0.02))
