#!/usr/bin/env python3
"""
Tasks
Alter a code into a new function task_wait_n
"""

import asyncio
from typing import List
task_wait_random = __import__('3-tasks').task_wait_random

get = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    Function task_wait_n
    Alter code
    """

    delays: List[float] = []
    all_delays: List[float] = []
    for i in range(n):
        delays.append(task_wait_random(max_delay))
    for delay in asyncio.as_completed(delays):
        earliest_result = await delay
        all_delays.append(earliest_result)
    return all_delays
