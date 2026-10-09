import asyncio
from functools import wraps
import time

import httpx
from pydantic import ValidationError

from GitHub_Profile_Analyzer.api import get_user
from GitHub_Profile_Analyzer.models import GitHubUser
from GitHub_Profile_Analyzer.file_utils import get_project_root,load_users,save_json


def Time(func):
    """时间装饰器"""
    @wraps(func)
    async def wrapper(*args,**kwarge):
        start = time.time()
        result =await func(*args,**kwarge)
        end = time.time()
        return result
    return wrapper



async def process_user(
    client: httpx.AsyncClient,
    username: str,
)->GitHubUser|None:
    """处理单个用户：请求 + Pydantic 校验"""
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


def print_user(index: int, user: GitHubUser) -> None:
    """打印单个用户信息"""
    print(f"用户名: {user.login}")
    print(f"Followers: {user.followers}")
    print(f"公开仓库: {user.public_repos}")
    print(f"主页: {user.html_url}")
    print("-" * 40)
    

# 打印统计摘要
def print_summary(users: list[GitHubUser], failed_count: int) -> None:
    total_followers = sum(u.followers for u in users)
    avg_followers = total_followers / len(users) if users else 0
    top_user = max(users, key=lambda u: u.followers) if users else None

    print("\n统计摘要")
    print("-" * 40)
    print(f"总用户数:        {len(users) + failed_count}")
    print(f"成功:            {len(users)}")
    print(f"失败:            {failed_count}")
    print(f"总 Followers:    {total_followers}")
    print(f"平均 Followers:  {avg_followers:.1f}")
    if top_user:
        print(f"Top 用户:        {top_user.login} ({top_user.followers} followers)")



@Time
async def main():
    root = get_project_root()
    users_file = root / "data" / "users.txt"
    output_file = root/"output"/"github_users.json"

    usernames = load_users(users_file)
    if not usernames:
        print("没有可处理的用户名")
        return

    print(f"共 {len(usernames)} 个用户，开始并发查询...\n")

    # 并发请求
    async with httpx.AsyncClient() as client:
        task = [process_user(client,name)for name in usernames]
        results = await asyncio.gather(*task)

    # 过滤失败结果
    valid_users = [u for u in results if u is not None]
    failed_count = len(results) - len(valid_users)

    if not valid_users:
        print("没有任何成功的用户，程序退出")
        return

    valid_users.sort(key=lambda u: u.followers,reverse=True)

    # 打印
    print("=" * 40)
    for i, user in enumerate(valid_users, start=1):
        print_user(i, user)

    print_summary(valid_users, failed_count)

    # 保存
    data_to_save = [u.model_dump() for u in valid_users]
    if save_json(data_to_save, output_file):
        print(f"\n已保存到：{output_file}")


if __name__ == "__main__":
    asyncio.run(main())
