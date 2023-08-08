#!/usr/bin/env python3
"""Measure total runtime."""


from asyncio import gather
from time import perf_counter

async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """
    Measure total runtime.

    Returns:
          the total runtime

    """
    start_time: float = perf_counter()
    await gather(*[async_comprehension() for _ in range(4)])
    end_time: float = perf_counter()
    return end_time - start_time
