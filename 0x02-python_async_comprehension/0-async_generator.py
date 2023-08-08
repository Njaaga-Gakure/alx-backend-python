#!/usr/bin/env python3
"""Async generator module."""


from random import uniform
from typing import Generator
import asyncio


async def async_generator() -> Generator[float, None, None]:
    """Create an async generator that yield random values."""
    for _ in range(10):
        await asyncio.sleep(1)
        yield uniform(0, 10)
