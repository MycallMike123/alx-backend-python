#!/usr/bin/env python3

"""
Module that takes a list (mxd_list) of integers and floats
as arguments and returns their sum as a float.
"""

from typing import List, Union


def sum_mixed_list(mxd_list: List[Union[int, float]]) -> float:
    """
    Function to return the sum of a list of integers and floats
    """
    mixed_sum = 0.0

    for idx in mxd_list:
        if isinstance(idx, int) or isinstance(idx, float):
            mixed_sum += idx

    return mixed_sum
