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


wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> list[float]:
    """
    takes in 2 int arguments
    (in this order): n and max_delay.
    Spawn wait_random n times with the specified max_delay.

    wait_n should return the list of all the delays (float values).
    The list of the delays should be in ascending order
    without using sort() because of concurrency.
    """

    delays = await asyncio.gather(*(wait_random(max_delay) for _ in range(n)))
    return sorted(delays)


if __name__ == '__main__':
    import asyncio
    print(asyncio.run(wait_n(5, 5)))
    print(asyncio.run(wait_n(10, 7)))
    print(asyncio.run(wait_n(10, 0)))
