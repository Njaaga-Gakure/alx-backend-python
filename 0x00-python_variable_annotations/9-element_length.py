#!/usr/bin/env python3
"""Annotate a function module."""

from typing import List, Tuple, Iterable, Sequence


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    Make a tuple containing a sequence and an integer.

    args:
        lst (list): a list of sequences i.e list, tuples etc
    Returns:
        a tuple containing a sequence and an int

    """
    return [(i, len(i)) for i in lst]
