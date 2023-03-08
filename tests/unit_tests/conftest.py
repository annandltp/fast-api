import pytest
from app.services.user import UserService

@pytest.fixture
def profile_infos():
    val = {
        0: {
            "short_description": "My Bio Description",
            "long_bio": "This is our longer bio"
        }
    }
    return val

@pytest.fixture
def users_content():
    val = {
        0: {
            "liked_posts": [1] * 2,
        }
    }
    return val

@pytest.fixture(scope="module")
def testing_fixture():
    print("Initializing fixture")
    return 'a'

@pytest.fixture
def user_service(profile_infos, users_content):
    user_service = UserService(profile_infos, users_content)
    return user_service