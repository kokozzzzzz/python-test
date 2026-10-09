# GitHub Profile Analyzer（GitHub 用户信息批量分析）

这是 Python 练习项目的综合实战模块，把 Day 2（API 请求与数据保存）、Day 4（类型注解与 Pydantic 校验）、Day 5（httpx 异步并发）、Day 7（模块拆分与测试）的知识点整合成一个可运行的小工具。

程序从 `data/users.txt` 读取用户名列表，并发请求 GitHub API，校验数据后按 followers 降序排序，打印每个用户的信息与统计摘要，并把结果保存到 `output/github_users.json`。

## 项目内容

- 模块化拆分：`api.py`（网络请求）、`models.py`（数据模型）、`file_utils.py`（文件读写）、`main.py`（流程控制）
- 使用 `httpx.AsyncClient` + `asyncio.gather()` 并发请求多个用户，而不是逐个串行等待
- 使用 Pydantic `GitHubUser` 校验 API 返回字段（login / followers / public_repos / html_url），字段非法时跳过该用户
- 分类处理请求异常：超时、404 用户不存在、401 Token 失效、403 限流、其他网络错误
- 单个用户失败不会中断整体流程，统计摘要中单独记录失败数量
- 使用自定义计时装饰器 `Time`（`functools.wraps` + `await`）包裹 `main`
- 统计摘要包含：总用户数、成功 / 失败数、总 Followers、平均 Followers、Top 用户
- 结果通过 `model_dump()` 转为 dict 后保存 JSON（`ensure_ascii=False` + `indent=4`）

## 项目结构

```text
GitHub_Profile_Analyzer/
├── __init__.py
├── main.py           # 入口：并发查询、打印、统计、保存
├── api.py            # 异步封装 GitHub API：get_user()
├── models.py         # Pydantic 模型 GitHubUser
└── file_utils.py     # get_project_root / load_users / save_json
```

## 环境

与项目根目录共享同一个虚拟环境：

- Python 3.13.14
- 依赖：`httpx`、`pydantic`、`python-dotenv`

## 配置说明

运行前必须配置 GitHub Token：

1. 在项目根目录复制 `.env_example` 为 `.env`，填入真实值：

   ```env
   GITHUB_TOKEN=你的GitHub个人访问令牌
   ```

2. `api.py` 启动时通过 `load_dotenv()` 读取根目录 `.env`，再用 `os.getenv("GITHUB_TOKEN")` 取 Token；未配置会抛出 `ValueError` 并提示检查 `.env`。

3. 请求头需要携带 `Authorization: token <TOKEN>` 与 `User-Agent`（GitHub API 强制要求提供 `User-Agent`）。

> **⚠️ 安全提示**：`.env` 由 `.gitignore` 忽略，Token 不要写进代码，也不要提交到 Git。

## 运行方式

在项目根目录以模块方式运行（保证包内导入正确）：

```bash
python -m GitHub_Profile_Analyzer.main
```

输入文件：`data/users.txt`，每行一个用户名，空行自动跳过。

## 输出说明

结果保存到 `output/github_users.json`，按 followers 从大到小排序：

```json
[
    {
        "login": "torvalds",
        "followers": 326945,
        "public_repos": 12,
        "html_url": "https://github.com/torvalds"
    },
    {
        "login": "gaearon",
        "followers": 93901,
        "public_repos": 301,
        "html_url": "https://github.com/gaearon"
    }
]
```
