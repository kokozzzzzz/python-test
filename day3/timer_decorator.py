import time
from functools import wraps

def timer(func):

    @wraps(func)

    def wrapper(*arg , **kwargs):
        start = time.time()

        result=func(*arg , **kwargs)

        end = time.time()

        print(f"{func.__name__}耗时：{end-start:.6f}秒")

        return result

    return wrapper


@timer
def work():
    total = 0
    for i in range(1000000):
        total+=i
    print(total)

@timer
def add(a,b):
    return a+b

work()

print(add(10,20))
