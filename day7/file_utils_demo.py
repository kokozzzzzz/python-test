
import json
from pathlib import Path


def save_user(data,username):
    """将用户信息保存在data目录中的JSON文件
    参数：
        data: GitHub API 返回的完整用户字典
        username：用户名

    """

    user_info = {
        "login" : data.get("login"),
        "public_repos" : data.get("public_repos"),
        "followers" : data.get("followers"),
        "html_url" : data.get("html_url")
    }

    root = Path(__file__).resolve().parent.parent
    output_dir = root / "output"
    output_dir.mkdir(parents=True,exist_ok=True)

    file_path = output_dir / f"{username}.json"

    try:
        with open(file_path,"w",encoding="utf-8") as f:
            json.dump(user_info,f,ensure_ascii=False,indent=4)
        print(f"用户信息已保存到：{file_path}")
    except PermissionError:
        print(f"没有权限写入文件：{file_path}")
    except OSError as e:
        print(f"写入文件失败：{e}")
    except TypeError as e:
        # json.dump 遇到不能序列化的类型会抛 TypeError
        print(f"数据无法序列化：{e}")
    except Exception:
        print("未知错误")


    

    