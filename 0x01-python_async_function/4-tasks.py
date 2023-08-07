#!/usr/bin/env python3
"""multiple coroutines at the same time with async."""

from typing import List
from asyncio import as_completed

task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
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
        delay: float = task_wait_random(max_delay)
        delay_list.append(delay)
    return [await delay for delay in as_completed(delay_list)]
