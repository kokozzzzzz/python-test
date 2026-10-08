import asyncio
import time
import httpx

async def get_user(client:httpx.AsyncClient,username:str):
    url = f"https://api.github.com/users/{username}"

    response = await client.get(url)

    return response.json()

async def main():
    users = [
        "octocat",
        "torvalds",
        "gaearon",
        "tj",
        "sindresorhus",
    ]

    start = time.time()
    
    async with httpx.AsyncClient() as client:
        tasks = [
            get_user(client, username)
            for username in users
        ]

        results = await asyncio.gather(*tasks)

        for data in results:
            print(
                data["login"],
                data["followers"]
            )

    end = time.time()
    print(f"同步耗时：{end - start:.2f} 秒")

asyncio.run(main())