import pytest
from app.schemas.user import FullUserProfile

@pytest.fixture(scope="module")
def valid_user_id() -> int:
    return 0

@pytest.fixture(scope="module")
def valid_user_delete_id() -> int:
    return 0

@pytest.fixture(scope="module")
def invalid_user_delete_id() -> int:
    return 1

@pytest.fixture(scope="module")
def sample_full_user_profile() -> FullUserProfile:
    return FullUserProfile(
        short_description="name",
        long_bio="The Username",
        username="This",
        liked_posts=[1,2,3]
    )

@pytest.fixture
def testing_rate_limit() -> int:
    return 25