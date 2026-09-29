import requests
import httpx
import os
from dotenv import load_dotenv

load_dotenv()

token = os.getenv("GITHUB_TOKEN")

if not token:
    raise ValueError("未找到 GITHUB_TOKEN，请检查 .env 文件是否配置正确")

headers = {
    "Authorization": "token {token}",
    "User-Agent": "MyApp/1.0"  # GitHub API 要求必须提供 User-Agent[reference:4]
}
url="https://api.github.com/users/kokozzzzzz"

response = requests.get(url,headers=headers)

print(response.status_code)

data = response.json()

print(data["login"])
print(data["public_repos"])
print(data["followers"])
print(data["html_url"])
print(data)


"""httpx试运行"""
# response = httpx.get(
#     "https://api.github.com/users/octocat"
# )
# data = response.json()

# print(response.status_code)
# print(data['login'])
# print(data['public_repos'])
# print(data["followers"])
# print(data["html_url"])
# print(data)