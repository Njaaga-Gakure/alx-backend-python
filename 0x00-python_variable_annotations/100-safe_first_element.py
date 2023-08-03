#!/usr/bin/env python3
"""Duck typing module."""

from typing import Sequence, Any, Union


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """
    Argument code with correct duck-typed annotations.

    args:
        lst (Sequence): sequence containing data of any type
    Return:
        either element of any type or None

    """
    if lst:
        return lst[0]
    else:
        return None
