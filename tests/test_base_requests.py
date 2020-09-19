import pytest
from requests import Response

from parallel_requests.base_requests import request

from .conftest import FakeFuture


@pytest.fixture
def mock_parallel_requests_requests_request(mocker, helpers):
    mock_parallel_requests_requests_request = mocker.patch(
        "parallel_requests.base_requests.futures"
    )
    mock_parallel_requests_requests_request.executor.return_value.submit = None
    mock_parallel_requests_requests_request.as_completed.return_value = [FakeFuture]
    return mock_parallel_requests_requests_request


def test_request(mock_parallel_requests_requests_request, helpers):
    responses = request(
        method_args=[{"url": "https://www.python.org", "method": "post"}],
    )

    assert isinstance(responses[0], Response)
    assert isinstance(helpers().response_object_200_msg(), Response)
