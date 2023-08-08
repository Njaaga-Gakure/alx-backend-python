#!/usr/bin/env python3
"""Async comprehension module."""


from typing import List


async_generator = __import__("0-async_generator").async_generator


async def async_comprehension() -> List[float]:
    """
    Return a list asynchronously from an async generator.

    Returns:
         a list of random floats from 0 to 10

    """
    return [num async for num in async_generator()]
