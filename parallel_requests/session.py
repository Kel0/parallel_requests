"""
parallel_requests.session
~~~~~~~~~~~~~~~~~~~~~~~~~

Provide extended requests.session library
"""

from concurrent import futures
from concurrent.futures import Future
from typing import Any, Dict, List, Set

import requests

from .base_requests import ListResponse


class Session(requests.Session):
    def __init__(self):
        super().__init__()

    def parallel_request(
        self, method_args: List[Dict[str, Any]], max_workers: int = 5
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

    def parallel_post(
        self,
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

        return self.parallel_request(method_args=method_args, max_workers=max_workers)

    def parallel_get(
        self,
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

        return self.parallel_request(method_args=method_args, max_workers=max_workers)

    def parallel_options(
        self,
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

        return self.parallel_request(method_args=method_args, max_workers=max_workers)

    def parallel_put(
        self,
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

        return self.parallel_request(method_args=method_args, max_workers=max_workers)

    def parallel_patch(
        self,
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

        return self.parallel_request(method_args=method_args, max_workers=max_workers)

    def parallel_head(
        self,
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

        return self.parallel_request(method_args=method_args, max_workers=max_workers)

    def parallel_delete(
        self,
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

        return self.parallel_request(method_args=method_args, max_workers=max_workers)


def extended_session():
    """
    Returns a :class:`Session` for context-management.

    :rtype: Session
    """
    return Session()
