#!/usr/bin/env python3
"""multiple coroutines at the same time with async."""


from typing import List
from asyncio import as_completed

wait_random = __import__("0-basic_async_syntax").wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    Return a sorted list with time delays.

    args:
       n (int): number of time to call the wait_random function
       max_delay: (int): upper limit of the random delay
    Returns:
          sorted list of time delays
    """
    delay_list: List[float] = []
    for _ in range(n):
        delay: float = wait_random(max_delay)
        delay_list.append(delay)
    return [await delay for delay in as_completed(delay_list)]
