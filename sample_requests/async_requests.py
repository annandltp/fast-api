import aiohttp
import asyncio



# RAW
async def sample_async_get_request():
    async with aiohttp.ClientSession() as session:
        async with session.get("http://127.0.0.1:8000/user/0") as response:
            print(response.status)
            print(response.headers)
            print(await response.json())

async def sample_async_post_request():
    sample_data_to_send = {
        "name": "bobi",
        "liked_posts": [
            0, 1, 2
        ],
        "short_description": "string",
        "long_bio": "string"
    }
    async with aiohttp.ClientSession() as session:
        async with session.post("http://127.0.0.1:8000/user", json=sample_data_to_send) as response:
            print(response.status)
            print(response.headers)
            print(await response.json())

# asyncio.run(sample_async_post_request())