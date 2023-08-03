#!/usr/bin/env python3
"""Return a function module."""

from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    Return a function that return the product of two floats.

    args:
        multiplier (float): a float
    Returns:
        a function that multiplies two floats

    """
    def mult(num: float):
        return num * multiplier
    return mult
