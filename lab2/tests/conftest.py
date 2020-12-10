from starlette.testclient import TestClient
from pytest import fixture

@fixture(scope="session")
def test_client():
    from app.server import app
    with TestClient(app) as test_client:
        yield test_client