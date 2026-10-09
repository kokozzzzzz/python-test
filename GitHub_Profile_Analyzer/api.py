import os

from dotenv import load_dotenv
import httpx



BASE_URL = "https://api.github.com"
load_dotenv()

TOKEN = os.getenv("GITHUB_TOKEN")

if not TOKEN:
    raise ValueError("未找到 GITHUB_TOKEN，请检查 .env 文件是否配置正确")

HEADERS = {
        "Authorization": f"token {TOKEN}",
        "User-Agent": "MyApp/1.0"  # GitHub API 要求必须提供 User-Agent[reference:4]
    }


async def get_user(
    client: httpx.AsyncClient,
    username: str
)->dict|None:
    """根据用户名请求Github API，返回用户信息的字典

    请求成功返回 dict；
    用户不存在返回 None；
    其他异常返回 None。
    """
    
    url = f"{BASE_URL}/users/{username}"

    try:
        response = await client.get(url,headers=HEADERS)
        response.raise_for_status()
        return response.json()
    except httpx.TimeoutException:
        print(f"[超时] {username}")
        return None
    except httpx.HTTPStatusError as e:
        status = e.response.status_code
        if status == 404:
            print(f"[未找到] {username}")
        elif status == 401:
            print(f"[认证失败] {username}，Token 可能已失效")
        elif status == 403:
            print(f"[限流] {username}，请求被拒绝")
        else:
            print(f"[HTTP {status}] {username}")
        return None
    except httpx.HTTPError as e:
        print(f"[网络错误] {username}:{e}")
        return None



