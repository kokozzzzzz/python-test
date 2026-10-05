
from pathlib import Path
import time

def timer(func):
    """装饰器：统计被装饰函数的执行耗时。"""
    def wrapper(*args,**kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"函数{func.__name__}耗时：{end-start:.6f}秒")
        return result

    return wrapper
        
def read_users(file_path):
    """生成器：逐行读取用户文件，每次yield一个非空用户名。"""
    path = Path(file_path)
    if not path.exists():
        print("文件不存在:{file_path}")
        return

    with open(path,"r",encoding="utf-8") as f:
        for line in f:
            username = line.strip()
            if username:
                yield username


@timer
def process_users():
    for username in read_users("data/users.txt"):
        print(username)

if __name__ == "__main__":
    process_users()