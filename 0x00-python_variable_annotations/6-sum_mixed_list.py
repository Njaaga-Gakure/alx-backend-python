#!/usr/bin/env python3
"""Sum mixed lis module."""


from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """
    Sum element of a list.

    args:
        mxd_lst (list): a list of floats and integers
    Returns:
        Sum of the elements as a float

    """
    sum: float = 0.0
    for num in mxd_lst:
        sum += num
    return sum
