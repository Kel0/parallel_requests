"""
This module provides only two HTTP request methods benchmarks
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

1. Parallel GET request - ~12.961835145950317
2. Parallel POST request - ~10.807614088058472

1. Synchronous GET request - ~41.12413253263
2. Synchronous POST request - ~40.95021678264


Notice that speed of requests depends to your internet connection speed

session.py requests have the same execution time
"""
from time import time

import parallel_requests


def timer(func):
    def wrapper(*args, **kwargs):
        start = time()
        func(*args, **kwargs)
        end = time()
        print(end - start)

    return wrapper


@timer
def benchmark_get_request():
    parallel_requests.get(
        method_args=[{"url": "https://www.python.org"} for _ in range(100)]
    )


@timer
def benchmark_post_request():
    parallel_requests.post(
        method_args=[{"url": "https://www.python.org"} for _ in range(100)]
    )


benchmark_get_request()  # ~12.961835145950317
benchmark_post_request()  # ~10.807614088058472
