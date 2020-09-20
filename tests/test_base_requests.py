import pytest
from requests import Response

from .conftest import FakeFuture

from parallel_requests.base_requests import (  # isort:skip
    delete,
    get,
    head,
    options,
    patch,
    post,
    put,
    request,
)


@pytest.fixture
def mock_parallel_requests_requests_future(mocker, helpers):
    mock_parallel_requests_requests_future = mocker.patch(
        "parallel_requests.base_requests.futures"
    )
    mock_parallel_requests_requests_future.executor.return_value.submit = None
    mock_parallel_requests_requests_future.as_completed.return_value = [FakeFuture]
    return mock_parallel_requests_requests_future


@pytest.mark.parametrize("method", ["post", "get", "head", "options", "put", "patch"])
def test_request(mock_parallel_requests_requests_future, method, helpers):
    responses = request(
        method_args=[{"url": "https://www.python.org", "method": method}],
    )

    assert all(response for response in responses if isinstance(response, Response))


def test_post(mock_parallel_requests_requests_future, helpers):
    responses = post(
        method_args=[{"url": "https://www.python.org"}],
    )

    assert all(response for response in responses if isinstance(response, Response))


def test_get(mock_parallel_requests_requests_future, helpers):
    responses = get(
        method_args=[{"url": "https://www.python.org"}],
    )

    assert all(response for response in responses if isinstance(response, Response))


def test_options(mock_parallel_requests_requests_future, helpers):
    responses = options(
        method_args=[{"url": "https://www.python.org"}],
    )

    assert all(response for response in responses if isinstance(response, Response))


def test_put(mock_parallel_requests_requests_future, helpers):
    responses = put(
        method_args=[{"url": "https://www.python.org"}],
    )

    assert all(response for response in responses if isinstance(response, Response))


def test_patch(mock_parallel_requests_requests_future, helpers):
    responses = patch(
        method_args=[{"url": "https://www.python.org"}],
    )

    assert all(response for response in responses if isinstance(response, Response))


def test_delete(mock_parallel_requests_requests_future, helpers):
    responses = delete(
        method_args=[{"url": "https://www.python.org"}],
    )

    assert all(response for response in responses if isinstance(response, Response))


def test_head(mock_parallel_requests_requests_future, helpers):
    responses = head(
        method_args=[{"url": "https://www.python.org"}],
    )

    assert all(response for response in responses if isinstance(response, Response))
