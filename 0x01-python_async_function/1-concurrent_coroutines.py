#!/usr/bin/env python3

"""
Module that contains Asynchronous coroutine that takes in two arguments
and returns a list of delayed float values
"""

import asyncio
from typing import List

wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    Asynchronous coroutine that takes in two
    arguments and returns a list of delayed float values.
    """

    delayed_tasks = []
    tasks = [wait_random(max_delay) for _ in range(n)]
    complete = asyncio.as_completed(tasks)
    for task in complete:
        result = await task
        delayed_tasks.append(result)
    return delayed_tasks
