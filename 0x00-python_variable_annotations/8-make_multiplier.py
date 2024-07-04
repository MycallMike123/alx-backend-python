#!/usr/bin/env python3

"""Module that takes a float multiplier as argument and
returns a function that multiplies a float by multiplier
"""

from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """Function to create and return a function that multiplies
    a float by the specified multiplier
    """
    def multiply(n: float) -> float:
        """Function that multiplies a float by multiplier"""
        return n * multiplier
    return multiply
