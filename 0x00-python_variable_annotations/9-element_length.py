#!/usr/bin/env python3

"""
Using duck typing
"""


from typing import Iterable, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    Duck typing tpe annotations
    """
    return [(i, len(i)) for i in lst]


if __name__ == '__main__':
    print(element_length.__annotations__)
