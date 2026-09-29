import json

from day2.api import get_user
from day2.file_utils import save_user

def main():
    username = input("请输入Github用户名：").strip()

    if not username:
        print("用户名不能为空")
        return
        
    data = get_user(username)

    if data is None:
        print("获取用户信息失败")
        return
    
    print(f"登录名：{data['login']}")
    print(f"公开仓库数：{data['public_repos']}")
    print(f"粉丝数：{data['followers']}")
    print(f"主页：{data['html_url']}")
    save_user(data,username)


if __name__ == "__main__":
    main()

