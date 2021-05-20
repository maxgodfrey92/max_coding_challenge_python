from api.clients.gist_client import GistClient
import pytest


@pytest.fixture
def gist_client() -> GistClient:
    gist_client = GistClient()
    return gist_client
