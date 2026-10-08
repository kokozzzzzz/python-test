import json
from pathlib import Path


def get_project_root()->Path :
    """定位项目根目录：当前文件是 day5/file_utils.py，往上两级。"""
    return Path(__file__).resolve().parents[1]

def save_json(data,file_path:Path)->bool:
    """把 Python 对象保存为 JSON 文件。成功返回 True，失败返回 False。"""
    file_path = Path(file_path)
    file_path.parent.mkdir(parents=True,exist_ok=True)

    try:
        with open(file_path,"w",encoding="utf-8") as f:
            json.dump(data,f,ensure_ascii=False,indent=4)
        return True
    except OSError as e:
        print(f"[保存失败] {file_path}: {e}")
        return False
    except TypeError as e:
        print(f"[序列化失败] {e}")
        return False

def load_user(file_path:Path) -> list[str]:
    """从文本文件读取用户名列表，每行一个，跳过空行。"""
    path = Path(file_path)
    if not path.exists():
        print(f"[文件不存在] {file_path}")
        return []

    users = []
    try:
        with open(path,"r",encoding="utf-8") as f:
            for line in f:
                name=line.strip()
                if name:
                    users.append(name)
    except OSError as e:
        print(f"[读取失败] {file_path}: {e}")
        return []

    return users





