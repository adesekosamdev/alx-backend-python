#!/usr/bin/env python3
"""
Basics of async
Write asynchronous coroutine
Takes integer argument max_delay
"""

import random
import asyncio


async def wait_random(max_delay: int = 10) -> float:
    """
    Asynchronous coroutine
    max_delay
    """

    random_float = random.uniform(0, max_delay)
    await asyncio.sleep(random_float)
    return random_float
