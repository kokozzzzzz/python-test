import requests
import os
from dotenv import load_dotenv



BASE_URL="https://api.github.com"

def get_user(username):
    """根据用户名请求Github API，返回用户信息的字典

    请求成功返回 dict；
    用户不存在返回 None；
    其他异常返回 None。
    """
    load_dotenv()

    token = os.getenv("GITHUB_TOKEN")

    if not token:
        raise ValueError("未找到 GITHUB_TOKEN，请检查 .env 文件是否配置正确")

    headers = {
        "Authorization": "token {token}",
        "User-Agent": "MyApp/1.0"  # GitHub API 要求必须提供 User-Agent[reference:4]
    }

    url=f"{BASE_URL}/users/{username}"

    try:
        response = requests.get(url,headers=headers)
    except requests.RequestException as e:
        print(f"网络请求失败:{e}")
        return None
    
    if response.status_code==200:
        try:
            data = response.json()
            return data
        except ValueError as e:
            print(f"json返回值错误:{e}")
        
    elif response.status_code == 404:
        print(f"用户 {username} 不存在")
        return None
    else:
        print(f"请求失败，状态码：{response.status_code}")
        return None
    