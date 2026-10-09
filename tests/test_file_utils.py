import json
from day7.file_utils_demo import save_user


def test_save_user(tmp_path):
    path = tmp_path / "user"

    data = {
        "login":"kokozzzzzz",
        "public_repos":2,
        "followers":100,
        "html_url": None
    }

    save_user(data,path)

    real_path = tmp_path / "user.json"
    with open(real_path,"r",encoding="utf-8") as f:
        saved = json.load(f)

    assert saved == data



