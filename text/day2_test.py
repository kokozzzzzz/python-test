from pathlib import Path
import json
import requests
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

username = input("请输入用户名")

url="https://api.github.com/users/{username}"


response = requests.get(url,headers=headers)

data = response.json()

print(data['login'])
print(data['followers'])

user_info = {
    'login' : data['login'],
    'followers' : data['followers']
}

path = Path(__file__).resolve().parent.parent
output_dir = path / "output"
output_dir.mkdir(parents=True,exist_ok=True)

file_path = output_dir / f"{username}.json"

with open("file_path","w",encoding="utf-8") as f:
    json.dump(user_info,f,ensure_ascii=False,indent=4)
