#!/usr/bin/env python3

"""Module that contains a function takes an integer max_delay
and returns a asyncio.Task
"""

import asyncio
wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """
    task_wait_random is a function that takes an integer
    max_delay and returns an asyncio

    """
    # Create a task using asyncio.create_task() and return it
    return asyncio.create_task(wait_random(max_delay))
