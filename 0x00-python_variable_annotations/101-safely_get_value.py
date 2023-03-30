#!/usr/bin/env python3

"""
Given the parameters and return values, add type annotations to the function

Hint: look into TypeVar
"""


from typing import Union, Mapping, TypeVar, Any

T = TypeVar('T')


def safely_get_value(
        dct: Mapping, key: Any, default: Union[T, None] = None
        ) -> Union[None, T]:
    if key in dct:
        return dct[key]
    else:
        return default


if __name__ == '__main__':
    annotations = safely_get_value.__annotations__

    print("Here's what the mappings should look like")
    for k, v in annotations.items():
        print( ("{}: {}".format(k, v)))
