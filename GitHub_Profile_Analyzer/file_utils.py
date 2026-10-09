import json
from pathlib import Path

"""
def get_project_root() -> Path
def load_users(file_path: Path) -> list[str]
def save_json(data, file_path: Path) -> bool
"""





def get_project_root() -> Path:
    """定位项目路径,返回Path"""
    return Path(__file__).resolve().parents[1]

def load_users(file_path: Path) -> list[str]:
    """
    从文本文件读取用户名列表，每行一个，跳过空行。
    返回列表
    """
    path = Path(file_path)
    if not path.exists():
        print("[文件不存在]{file_path}")
        return []

    users = []

    try:
        with open(path,"r",encoding="utf-8") as f:
            for line in f:
                name = line.strip()
                if name:
                    users.append(name)
    except OSError as e:
        print(f"[读取失败] {file_path}: {e}")
        return []

    return users


def save_json(data, file_path: Path) -> bool:
    """把 Python 对象保存为 JSON 文件。成功返回 True，失败返回 False。"""
    path = Path(file_path)

    try:
        path.parent.mkdir(parents=True,exist_ok=True)
        with open(path,"w",encoding="utf-8") as f:
            json.dump(data,f,ensure_ascii=False,indent=4)
        return True
    except OSError as e:
        print(f"[保存失败] {path}: {e}")
        return False
    except TypeError as e:
        print(f"[序列化失败] {e}")
        return False




    



