#!/usr/bin/env python3
"""Return asyncio.Task."""


from asyncio import create_task, Task

wait_random = __import__("0-basic_async_syntax").wait_random


def task_wait_random(max_delay: int) -> Task:
    """
    Return asyncio.Task.

    args:
        max_delay (int): upper limit for random delay
        in the wait_random function
    Returns:
        async.Task

    """
    return create_task(wait_random(max_delay))
