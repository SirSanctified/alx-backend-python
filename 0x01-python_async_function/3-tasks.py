#!/usr/bin/env python3
"""
Create a task_wait_random function that takes an integer max_delay and returns
a asyncio.Task.
"""

import asyncio

wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """
    returns a asyncio.Task.
    """
    return asyncio.create_task(wait_random(max_delay))


if __name__ == '__main__':
    async def test(max_delay: int):
        task = task_wait_random(max_delay)
        await task
        print(task.__class__)

    asyncio.run(test(5))