"""
Parallel requests Library
~~~~~~~~~~~~~~~~~~~~~~

Parallel requests is a library which parallelize your requests.

POST HTTP request usage:
    >>> import parallel_requests
    >>> from typing import List
    >>> responses: parallel_requests.ListResponse = parallel_requests.post(
    >>>     method_args=[{"url": "https://www.python.org"}],
    >>>     max_workers=10
    >>> )
    >>> responses
    [<Response [200]>]

GET HTTP request usage
    >>> import parallel_requests
    >>> from typing import List
    >>> responses: parallel_requests.ListResponse = parallel_requests.get(
    >>>     method_args=[{"url": "https://www.python.org"}],
    >>>     max_workers=10
    >>> )
    >>> responses
    [<Response [200]>]

request function usage:
    >>> import parallel_requests
    >>> from typing import List
    >>> responses: parallel_requests.ListResponse = parallel_requests.request(
    >>>     method_args=[{"url": "https://www.python.org", "method": "post"}],
    >>>     max_workers=10
    >>> )
    >>> responses
    [<Response [200]>]

"""
from concurrent import futures
from concurrent.futures import Future
from typing import Any, Dict, List, Set

import requests

ListResponse = List[requests.Response]


def request(
    method_args: List[Dict[str, Any]],
    max_workers: int = 5,
) -> ListResponse:
    """
    Sends a :class: `Request <Request>`.

    :param method_args: Arguments which should be provided to requests.post feature.
    :param max_workers: Workers count. Effect to speed.
    :return loop_result: List of requests.Response objects
    """
    futures_: Set[Future]
    data: requests.Response
    loop_result: ListResponse = []

    with futures.ProcessPoolExecutor(max_workers=max_workers) as executor:
        futures_ = {
            executor.submit(requests.request, **method_args[index])
            for index in range(len(method_args))
        }

        for future in futures.as_completed(futures_):
            data = future.result()
            loop_result.append(data)

    return loop_result


def post(
    method_args: List[Dict[str, Any]],
    max_workers: int = 5,
) -> ListResponse:
    """
    Parallelized HTTP post requests.

    :param method_args: Arguments which should be provided to requests.post feature.
    :param max_workers: Workers count. Effect to speed.
    :return loop_result: List of requests.Response objects
    """
    for method_arg in method_args:
        method_arg["method"] = "post"

    return request(method_args=method_args, max_workers=max_workers)


def get(
    method_args: List[Dict[str, Any]],
    max_workers: int = 5,
) -> ListResponse:
    """
    Parallelized HTTP get requests.

    :param method_args: Arguments which should be provided to requests.post feature.
    :param max_workers: Workers count. Effect to speed.
    :return loop_result: List of requests.Response objects
    """
    for method_arg in method_args:
        method_arg["method"] = "get"

    return request(method_args=method_args, max_workers=max_workers)


def options(
    method_args: List[Dict[str, Any]],
    max_workers: int = 5,
) -> ListResponse:
    """
    Parallelized HTTP options requests.

    :param method_args: Arguments which should be provided to requests.post feature.
    :param max_workers: Workers count. Effect to speed.
    :return loop_result: List of requests.Response objects
    """
    for method_arg in method_args:
        method_arg["method"] = "options"

    return request(method_args=method_args, max_workers=max_workers)


def put(
    method_args: List[Dict[str, Any]],
    max_workers: int = 5,
) -> ListResponse:
    """
    Parallelized HTTP put requests.

    :param method_args: Arguments which should be provided to requests.post feature.
    :param max_workers: Workers count. Effect to speed.
    :return loop_result: List of requests.Response objects
    """
    for method_arg in method_args:
        method_arg["method"] = "put"

    return request(method_args=method_args, max_workers=max_workers)


def patch(
    method_args: List[Dict[str, Any]],
    max_workers: int = 5,
) -> ListResponse:
    """
    Parallelized HTTP patch requests.

    :param method_args: Arguments which should be provided to requests.post feature.
    :param max_workers: Workers count. Effect to speed.
    :return loop_result: List of requests.Response objects
    """
    for method_arg in method_args:
        method_arg["method"] = "patch"

    return request(method_args=method_args, max_workers=max_workers)


def delete(
    method_args: List[Dict[str, Any]],
    max_workers: int = 5,
) -> ListResponse:
    """
    Parallelized HTTP delete requests.

    :param method_args: Arguments which should be provided to requests.post feature.
    :param max_workers: Workers count. Effect to speed.
    :return loop_result: List of requests.Response objects
    """
    for method_arg in method_args:
        method_arg["method"] = "delete"

    return request(method_args=method_args, max_workers=max_workers)


def head(
    method_args: List[Dict[str, Any]],
    max_workers: int = 5,
) -> ListResponse:
    """
    Parallelized HTTP head requests.

    :param method_args: Arguments which should be provided to requests.post feature.
    :param max_workers: Workers count. Effect to speed.
    :return loop_result: List of requests.Response objects
    """
    for method_arg in method_args:
        method_arg["method"] = "head"

    return request(method_args=method_args, max_workers=max_workers)
