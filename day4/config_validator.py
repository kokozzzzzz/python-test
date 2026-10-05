import json
from pathlib import Path

from pydantic import BaseModel,Field, ValidationError


def load_config(file_path):
    """读取 JSON 文件，返回 dict。文件不存在或格式错误时返回 None。"""
    path = Path(file_path)

    if not path.exists():
        print(f"❌ 配置文件不存在：{file_path}")
        return None

    try:
        with open(path, "r", encoding="utf-8") as f:
            return json.load(f)
    except json.JSONDecodeError as e:
        print(f"❌ JSON 格式错误：{e}")
        return None
    except OSError as e:
        print(f"❌ 读取文件失败：{e}")
        return None

class LLMConfig(BaseModel):
    model : str = Field( min_length=1 )
    temperature : float = Field( ge=0, le=2 )
    max_tokens : int = Field( gt=0 )

def validate_config(data):
    """把 dict 转成 LLMConfig 模型。校验失败返回 None。"""
    try:
        config = LLMConfig(**data)
        return config
    except ValidationError as e:
        print("❌ 配置校验失败：")
        # e.errors() 返回错误列表，逐条打印更清楚
        for err in e.errors():
            field = ".".join(str(x) for x in err["loc"])
            print(f"  - 字段 [{field}]: {err['msg']}")
        return None
    except TypeError as e:
        # 比如 data 不是 dict，或者字段名不匹配
        print(f"❌ 参数错误：{e}")
        return None


def print_config(config):
    """打印验证后的配置。"""
    print("✅ 配置验证成功")
    print(f"Model: {config.model}")
    print(f"Temperature: {config.temperature}")
    print(f"Max Tokens: {config.max_tokens}")
    print()
    print("完整字典：")
    print(config.model_dump())


# data = load_config("data/llm_config.json")
# config = LLMConfig(**data)
# print(config.model_dump())


def main():
    root = Path(__file__).resolve().parents[1]
    config_file = root / "data" / "llm_config.json"

    data = load_config(config_file)
    if data is None:
        return

    config = validate_config(data)
    if config is None:
        return

    print_config(config)


if __name__ == "__main__":
    main()