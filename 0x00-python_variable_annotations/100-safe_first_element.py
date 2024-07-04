#!/usr/bin/env python3

"""
Module that augments the code with the correct duck-typed annotations
"""

from typing import List, Any, Sequence, Union


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """
    Function that returns either an element
    from the input_list or 'None'
    """

    if lst:
        return lst[0]
    else:
        return None
