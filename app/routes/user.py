from fastapi import APIRouter, HTTPException, Response, Depends
from app.schemas.user import (
    FullUserProfile,
    UserProfileInfo,
    MultipleUserResponse,
    CreateUserResponse
)
from app.services.user import UserService
from app.dependecies import rate_limit
import logging
import time

logger = logging.getLogger(__name__)
logging.basicConfig(
    format="%(levelname)-6s %(name)-15s %(asctime)s.%(msecs)03d %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
    filename="log.txt",
)
logger.setLevel(logging.WARNING)

console = logging.StreamHandler()
logger.addHandler(console)


def create_user_router(profile_infos: dict, users_content: dict) -> APIRouter:
    user_router = APIRouter(
        prefix="/user",
        tags=["user"],
        dependencies=[Depends(rate_limit)]
    )
    user_service = UserService(profile_infos, users_content)

    # ++++++++++++++++++++++++++++++++++++++++++++++ ROUTE ++++++++++++++++++++++++++++++++++++++++++++++
    @user_router.get("/all", response_model=MultipleUserResponse)
    async def get_all_users_paginated(start: int = 0, limit: int = 2):
        users, total = await user_service.get_all_users_with_pagination(start, limit)
        formatted_users = MultipleUserResponse(users=users, total=total)

        return formatted_users

    @user_router.get("/me", response_model=FullUserProfile)
    async def test_endpoint():
        full_user_profile = await user_service.get_user_info()

        return full_user_profile

    @user_router.get("/{user_id}", response_model=FullUserProfile)
    async def get_user_by_id(user_id: int, response: Response):
        # handle too many request
        # rate_limit(response)

        full_user_profile = await user_service.get_user_info(user_id)
        # response.headers["test-additional-header-value"] = "this is just something I'm adding"

        return full_user_profile

    @user_router.put("/{user_id}")
    async def update_user(user_id: int, full_profile_info: FullUserProfile):
        user_service.create_update_user(full_profile_info, user_id)
        return None

    @user_router.delete("/{user_id}")
    async def remove_user(user_id: int):
        # try:
        await user_service.delete_user(user_id)
        # except KeyError:
        #     logger.error(f"Non-Exist user_id: {user_id} was requested")
        #     raise HTTPException(status_code=404, detail={"msg": f"User doesn't exist", "user_id": user_id})
        # return None

    @user_router.post("", response_model=CreateUserResponse)
    async def add_user(full_profile_info: FullUserProfile):
        user_id = await user_service.create_update_user(full_profile_info)
        print("doc string of create_update_user:\n", user_service.create_update_user.__doc__)
        created_user = CreateUserResponse(user_id=user_id)
        return created_user

    @user_router.patch("/{user_id}", response_model=FullUserProfile)
    async def patch_user(user_id: int, user_profile_info: UserProfileInfo) -> FullUserProfile:
        if user_id in profile_infos:
            pass

        await user_service.partial_update_user(user_id, user_profile_info)
        return get_user_info(user_id)

    return user_router
