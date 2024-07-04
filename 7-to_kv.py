#!/usr/bin/env python3

"""
Module that contains a type-annotated function to_kv that takes a
string k and an int OR float v as arguments and returns a tuple
"""


from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    Function to return a tuple with a string
    and the square of an int or float
    """
    return (k, v ** 2)
