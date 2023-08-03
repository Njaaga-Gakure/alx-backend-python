#!/usr/bin/env python3
"""mypy validation module."""

from typing import List, Tuple


def zoom_array(lst: Tuple, factor: int = 2) -> List:
    """
    Make a list from a tuple.

    args:
        lst (tuple): a tuple
        factor (int): a integer
    Returns:
        Returns a list that depends on the factor

    """
    zoomed_in: List = [
        item for item in lst
        for i in range(factor)
    ]
    return zoomed_in


array = (12, 72, 91)

zoom_2x = zoom_array(array)
zoom_3x = zoom_array(array, 3)
