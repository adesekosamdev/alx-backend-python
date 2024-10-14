#!/usr/bin/env python3
"""
Tasks
function task_wait_random, takes integer argument max_delay
Returns a asyncio.Task
"""
import asyncio

wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """
    Function task_wait_random
    takes int argument max_delay
    Returns a async.Task
    """

    task = asyncio.create_task(wait_random(max_delay))
    return task
