#!/usr/bin/env python3
"""Sum list of floats module."""


from typing import List


def sum_list(input_list: List[float]) -> float:
    """
    Sum items in a numbers of floats.

    args:
        input_list (list): list of floats
    Returns:
        sum of the numbers in the list

    """
    sum: float = 0.0
    for num in input_list:
        sum += num
    return sum
