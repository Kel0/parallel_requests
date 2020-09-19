from dataclasses import dataclass

import pytest
from requests import Response


@dataclass
class FakeFuture:
    @staticmethod
    def result():
        return Helpers().response_object_200_msg()


class Helpers:
    def response_object_200_msg(self) -> Response:
        response = Response()
        response.status_code = 200
        return response


@pytest.fixture
def helpers():
    return Helpers
