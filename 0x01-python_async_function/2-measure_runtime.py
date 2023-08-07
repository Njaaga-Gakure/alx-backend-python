#!/usr/bin/env python3
"""Measure elapsed time."""


from time import time
from asyncio import run

wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """
    Measure elapsed time.

    args:
        n (int): no. of times to invoke function wait_random
        max_delay (int): upper limit of the random delay
    Return:
          total elapsed time divided by the no. of times
          the function was invoked

    """
    start: float = time()
    run(wait_n(n, max_delay))
    end: float = time()
    total_time: float = end - start
    return total_time / n
