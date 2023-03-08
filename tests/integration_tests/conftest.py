from fastapi.testclient import TestClient
from main import create_application
import pytest

@pytest.fixture(scope="session")
def testing_app():
    app = create_application()
    testing_app = TestClient(app)
    return testing_app