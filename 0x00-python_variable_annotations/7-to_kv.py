#!/usr/bin/env python3
"""string and int/float to tuple module."""


from typing import Tuple, Union


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    Create a tuple of a string and float.

    args:
        k (str): a string
        v (int | float): a string or a float
    Returns:
        a tuple with a string and a float

    """
    return k, v ** 2
