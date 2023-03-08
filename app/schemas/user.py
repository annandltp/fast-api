
from pydantic import BaseModel, Field
from typing import Optional


class User(BaseModel):
    username: str = Field(
        alias="name",
        title="The Username",
        description="This is the username of the user",
        # min_length=1,
        # max_length=20,
        default=None
    )
    liked_posts: list[int] = Field(
        description="Array of post ids the user liked",
        # min_items=2,
        # max_items=10
    )


class FullUserProfile(User):
    short_description: str
    long_bio: str


class MultipleUserResponse(BaseModel):
    users: list[FullUserProfile]
    total: int


class CreateUserResponse(BaseModel):
    user_id: int


class UserProfileInfo(BaseModel):
    short_description: str
    long_bio: str
