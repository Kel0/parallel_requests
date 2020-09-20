import pytest
from requests import Response

from parallel_requests.session import Session, extended_session

from .conftest import FakeFuture


@pytest.fixture
def mock_parallel_requests_session_future(mocker, helpers):
    mock_parallel_requests_session_future = mocker.patch(
        "parallel_requests.session.futures"
    )
    mock_parallel_requests_session_future.executor.return_value.submit = None
    mock_parallel_requests_session_future.as_completed.return_value = [FakeFuture]
    return mock_parallel_requests_session_future


def test_extended_session():
    with extended_session() as session:
        assert isinstance(session, Session)

    session = extended_session()
    assert isinstance(session, Session)
    session.close()


@pytest.mark.parametrize("method", ["post", "get", "head", "options", "put", "patch"])
def test_session_parallel_request(
    mock_parallel_requests_session_future, method, helpers
):
    with Session() as session:
        responses = session.parallel_request(
            method_args=[{"url": "https://www.python.org", "method": method}],
        )

        assert all(response for response in responses if isinstance(response, Response))


def test_session_parallel_post(mock_parallel_requests_session_future, helpers):
    with Session() as session:
        responses = session.parallel_post(
            method_args=[{"url": "https://www.python.org"}],
        )

        assert all(response for response in responses if isinstance(response, Response))


def test_session_parallel_get(mock_parallel_requests_session_future, helpers):
    with Session() as session:
        responses = session.parallel_get(
            method_args=[{"url": "https://www.python.org"}],
        )

        assert all(response for response in responses if isinstance(response, Response))


def test_session_parallel_options(mock_parallel_requests_session_future, helpers):
    with Session() as session:
        responses = session.parallel_options(
            method_args=[{"url": "https://www.python.org"}],
        )

        assert all(response for response in responses if isinstance(response, Response))


def test_session_parallel_put(mock_parallel_requests_session_future, helpers):
    with Session() as session:
        responses = session.parallel_put(
            method_args=[{"url": "https://www.python.org"}],
        )

        assert all(response for response in responses if isinstance(response, Response))


def test_session_parallel_patch(mock_parallel_requests_session_future, helpers):
    with Session() as session:
        responses = session.parallel_patch(
            method_args=[{"url": "https://www.python.org"}],
        )

        assert all(response for response in responses if isinstance(response, Response))


def test_session_parallel_head(mock_parallel_requests_session_future, helpers):
    with Session() as session:
        responses = session.parallel_head(
            method_args=[{"url": "https://www.python.org"}],
        )

        assert all(response for response in responses if isinstance(response, Response))


def test_session_parallel_delete(mock_parallel_requests_session_future, helpers):
    with Session() as session:
        responses = session.parallel_delete(
            method_args=[{"url": "https://www.python.org"}],
        )

        assert all(response for response in responses if isinstance(response, Response))
