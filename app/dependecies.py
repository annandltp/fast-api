from fastapi import APIRouter, HTTPException, Response, Depends
from app.schemas.user import (
    FullUserProfile,
    UserProfileInfo,
    MultipleUserResponse,
    CreateUserResponse
)
from app.services.user import UserService
import logging
import time

count = 0
start_time = time.time()
reset_interval = 10
limit = 5

def rate_limit(response: Response) -> None:
    global start_time
    global count

    if time.time() > start_time + reset_interval:
        start_time = time.time()
        count = 0

    if count >= limit:
        raise HTTPException(status_code=429, detail={
            "error": "Rate limit exceeded",
            "timeout": round(start_time + reset_interval - time.time(), 2) + 0.01
        })

    count += 1
    response.headers["X-app-rate-limit"] = f"{count}:{limit}"

    return Response
