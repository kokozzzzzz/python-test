
def add(a:int,b:int) -> int:
    return a+b

def get_names(users:list[dict[str:str]]) -> list[str]:
    names = []
    for user in users:
        names.append(user["name"])

    return names

def find_user(users: list[str],name: str) -> str | None:
    if name in users:
        return name

    return None

users = [
    {"name": "Alice"},
    {"name": "Bob"},
]

print(get_names(users))
