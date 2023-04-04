#!/usr/bin/env python3

"""
Import wait_random from the previous python file
and write an async routine called wait_n that takes in 2 int arguments
(in this order): n and max_delay.
Spawn wait_random n times with the specified max_delay.

wait_n should return the list of all the delays (float values).
The list of the delays should be in ascending order
without using sort() because of concurrency.
"""

import asyncio
from typing import List

wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    takes in 2 int arguments
    (in this order): n and max_delay.
    Spawn wait_random n times with the specified max_delay.

    wait_n should return the list of all the delays (float values).
    The list of the delays should be in ascending order
    without using sort() because of concurrency.
    """

    delays = [wait_random(max_delay) for i in range(1, n + 1)]
    results = await asyncio.gather(*delays, return_exceptions=True)
    results = [result for result in results if not isinstance(result, Exception)]
    return sorted(results)


if __name__ == '__main__':
    print(asyncio.run(wait_n(5, 5)))
    print(asyncio.run(wait_n(10, 7)))
    print(asyncio.run(wait_n(10, 0)))
