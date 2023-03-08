import os

class Config:
    DB_HOST = os.getenv("my.database.com")
    DB_USERNAME = os.getenv("user1")
    DB_PASSWORD = os.getenv("password")
