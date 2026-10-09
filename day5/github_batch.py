import asyncio
from functools import wraps
import time

from pydantic import BaseModel, Field,ValidationError
from pathlib import Path

import httpx

from day5.api import get_user
from day5.file_utils import get_project_root, load_user, save_json



def Time(func):
    """计算函数func运行时间"""
    @wraps(func)
    async def wrapper(*args,**kwargs):
        start = time.time()
        result = await func(*args,**kwargs)
        end = time.time()
        print(f"\n[耗时] {func.__name__} 用时 {end - start:.2f} 秒\n")
        return result
    return wrapper


class GitHubUser(BaseModel):
    login:str
    followers:int = Field(ge=0)
    public_repos:int
    html_url:str


async def process_user(
    client:httpx.AsyncClient,
    username:str
)->GitHubUser | None:
    """处理单个用户：请求 + 转换成模型"""
    data = await get_user(client,username)
    if data is None:
        return None

    try:
        return GitHubUser(
            login=data["login"],
            followers=data["followers"],
            public_repos=data["public_repos"],
            html_url=data["html_url"],
        )
    except (KeyError, ValidationError) as e:
        print(f"[数据异常] {username}: {e}")
        return None

def print_summary(users):
    total_followers = sum(
        user.followers for user in users
    )

    print(f"总 followers: {total_followers}")

@Time
async def main():
    root = get_project_root()
    users_file = root / "data" / "users.txt"
    output_file = root / "output" / "github_users.json"

    users = load_user(users_file)

    if not users:
        print("没有可处理的用户名")
        return

    print(f"共 {len(users)} 个用户，开始并发查询...\n")

    async with httpx.AsyncClient() as client:
        tasks = [process_user(client,username) for username in users]
        results = await asyncio.gather(*tasks)

    valid_users = [u for u in results if u is not None]

    print("=" * 40)
    for user in valid_users:
        print(f"用户名: {user.login}")
        print(f"Followers: {user.followers}")
        print(f"公开仓库: {user.public_repos}")
        print(f"主页: {user.html_url}")
        print("-" * 40)

    print_summary(valid_users)

    data_to_save = [u.model_dump() for u in valid_users]
    if save_json(data_to_save,output_file):
        print(f"已保存到：{output_file}")


if __name__ == "__main__":
    asyncio.run(main())
