import pytest

from test_api.src.client.api_client import ApiClient


@pytest.fixture
def api_client():
    return ApiClient()
