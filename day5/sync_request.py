import time
import httpx


users = [
    "octocat",
    "torvalds",
    "gaearon",
    "tj",
    "sindresorhus",
]

start = time.time()

for username in users:
    url = f"https://api.github.com/users/{username}"

    response = httpx.get(url)

    data = response.json()

    print(
        data["login"],
        data["followers"]
    )

end = time.time()

print(f"同步耗时：{end - start:.2f} 秒")