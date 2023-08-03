#!/usr/bin/env python3
"""TypeVar module."""

from typing import Mapping, Any, Union, TypeVar


T = TypeVar("T")


def safely_get_value(dct: Mapping, key:
                     Any, default: Union[T, None] = None) -> Union[Any, T]:
    """
    Return a value from a dictionary.

    args:
        dct (dict): a dictionary
        key (any): a key of any data type
    default: value defaulted to None
    Returns:
        the value in the dict that corresponds to the key or None
    """
    if key in dct:
        return dct[key]
    else:
        return default
