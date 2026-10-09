# Python 项目练习（Day 1 - Day 7）

这是一个 Python 学习练习项目，按照“每日一个独立模块”的方式组织。每天的内容作为独立的迷你项目存放在对应目录下，共享同一个虚拟环境。

## 项目内容

### Day 1：学生成绩管理（面向对象与数据持久化）
- 使用 Python 类封装 `Student` 对象，包含姓名、年龄和分数。
- 实现对象的格式化输出（`__str__`）。
- 使用 `pathlib` 管理文件路径，将数据保存为 `data/students.json`。
- 练习文件读写与基础异常处理。

### Day 2：GitHub 用户 API 请求与数据处理
- 使用 `requests` (和 `httpx`) 发送 GET 请求，获取 GitHub 用户信息。
- 从 API 返回的大量数据中筛选所需字段（login, public_repos, followers, html_url）。
- 使用 `pathlib` 和 `json.dump` 将筛选后的数据保存到 `output/用户名.json`。
- 使用 `.env` 文件管理敏感凭证（GitHub Personal Access Token），避免硬编码和泄露。
- 初步实现模块化拆分：`api.py`（网络请求）、`file_utils.py`（文件保存）、`main.py`（流程控制）。

### Day 3：装饰器、生成器与上下文管理器
- 理解装饰器的本质：`@decorator` 等价于 `func = decorator(func)`
- 掌握 `*args` 和 `**kwargs` 在装饰器中的作用
- 会用 `functools.wraps` 保留原函数信息
- 理解生成器与 `yield`：逐步产生数据，而不是一次性返回
- 理解上下文管理器：`with` 如何自动管理资源
- 能自己写出 `__enter__` 和 `__exit__`
- 完成一个综合练习，把装饰器、生成器、`with` 串起来

### Day 4：类型注解、dataclass 与 Pydantic 数据校验
- 掌握基础类型注解：为函数参数和返回值标注类型，如 `def add(a: int, b: int) -> int`
- 使用 `list[dict[str, str]]` 描述嵌套数据结构
- 使用 `str | None` 表示可能为空的返回值
- 使用 `@dataclass` 自动生成 `__init__` 和 `__repr__`，减少样板代码
- 使用 Pydantic `BaseModel` 和 `Field` 对字段做校验（如 `gt` / `le` / `min_length`）
- 理解校验失败时 `ValidationError` 的错误信息结构
- 使用 `model_dump()` 和 `model_dump_json()` 在模型与 dict / JSON 之间转换
- 完成一个综合练习：读取并校验 `data/llm_config.json` 中的 LLM 配置

### Day 5：httpx 异步请求与 asyncio 并发
- 使用 `httpx` 发送同步请求，作为耗时对照基准
- 理解 `async` / `await`：协程的定义与调用方式
- 使用 `asyncio.gather()` 并发执行多个任务，对比串行与并发的耗时差异
- 使用 `httpx.AsyncClient` 复用连接发起异步请求
- 为异步函数编写计时装饰器（`functools.wraps` + `await`）
- 使用 Pydantic `BaseModel` 校验并筛选 API 返回字段（login / followers / public_repos / html_url）
- 完成一个综合练习：读取 `data/users.txt` 中的用户名，并发请求 GitHub API 并保存到 `output/github_users.json`

### Day 6：Git 分支管理与 Linux / WSL 环境实践
- 熟练使用 `git status / add / commit / log / diff / branch / switch / merge / push / pull`
- 创建 `feature/github-summary` 分支开发新功能：为 Day 5 批量查询新增 `print_summary()` 统计总 followers，切回 `main` 后完成 `git merge`
- 主动制造并解决一次 merge conflict，理解 `<<<<<<< HEAD`、`=======`、`>>>>>>> branch` 的含义
- 使用 `git log --oneline --graph --all` 查看分支与合并历史
- Linux 基础命令：`pwd / ls / cd / mkdir / touch / cat / grep / find / ps / kill`，以及管道 `|` 与重定向 `>` / `>>`
- 使用 `curl` 在终端直接请求 GitHub API，查看 JSON 内容与响应头
- 环境变量：`export` 与 `echo $VAR`，Python 中通过 `os.getenv()` 读取（day6/os_test.py）
- 新增 `.env_example` 环境变量模板并提交 Git，`.env` 继续由 `.gitignore` 忽略
- 在 WSL 中从零 clone 项目，创建 `python3 -m venv .venv`，`pip install -r requirements.txt` 后终端运行项目，验证不依赖 Windows IDE 环境

### Day 7：pytest 基础测试
- 理解 pytest 的用例发现规则：文件名需为 `test_*.py`（或 `*_test.py`），函数名以 `test_` 开头才会被自动收集
- 用最朴素的 `assert` 编写断言，完成第一个测试 `test_add`
- 使用 `@pytest.mark.parametrize` 参数化测试：一份用例覆盖多组输入（1+2、2+3、10+20、0+0）
- 使用 `pytest.raises(ValidationError)` 断言非法输入抛出预期异常（如 followers 为负数）
- 使用内置 fixture `tmp_path` 在临时目录中测试 `save_user` 的 JSON 写入，不污染真实的 `output/` 目录
- 把 Pydantic 模型 `GitHubUser` 拆到 `day7/models.py`，待测函数 `save_user` 拆到 `day7/file_utils_demo.py`，便于被测试导入
- 在项目根目录放置 `conftest.py`，让 pytest 把项目根加入 `sys.path`，解决 `from day7.models import ...` 的导入问题
- 将测试代码集中到 `tests/` 目录，与每日练习代码分离
- `requirements.txt` 新增 `pytest`，当前 7 个用例全部通过

## 项目结构

```text
python-test/
├── .env                  # 本地私有配置，存放 Token（不提交至 Git）
├── .env_example          # 环境变量模板（可提交至 Git）
├── .gitignore
├── requirements.txt
├── README.md
├── conftest.py           # 空文件，让 pytest 把项目根加入 sys.path
├── data/
|   ├── test.txt          # Day3 生成器测试数据
|   ├── users.txt         # Day3 / Day5 用户数据
|   ├── llm_config.json   # Day4 待校验的配置文件
│   └── students.json     # Day1 保存的学生数据
├── day1/                 # Day 1 独立迷你项目
│   ├── __init__.py
│   ├── main.py           # Day1 入口文件
│   └── student.py        # Student 类定义
├── day2/                 # Day 2 github姓名获取
│   ├── __init__.py
│   ├── api_demo.py       # 接口测试调试脚本
│   ├── api.py            # 负责网络请求
│   ├── file_utils.py     # 负责数据筛选与保存
│   └── main.py           # Day2 入口文件
|
├── day3/                 # Day3 装饰器、生成器、上下文管理器
│   ├── __init__.py
│   ├── timer_decorator.py  # 时间装饰器
│   ├── generator_demo.py   # 文件生成器
│   ├── file_context.py     # 上下文管理器
│   └── day3_demo.py        # Day3 综合小练习
|
├── day4/                 # Day4 类型注解、dataclass、Pydantic
│   ├── type_hint_demo.py     # 类型注解练习
│   ├── dataclass_demo.py     # dataclass 练习
│   ├── pydantic_demo.py      # Pydantic 基础练习
│   └── config_validator.py   # Day4 综合练习：配置校验
|
├── day5/                 # Day5 httpx 异步请求与 asyncio 并发
│   ├── async_demo.py         # asyncio 基础演示（gather 并发）
│   ├── sync_request.py       # 同步请求基准
│   ├── async_request.py      # 异步并发请求
│   ├── api.py                # 异步 GitHub API 封装
│   ├── file_utils.py         # 路径定位、JSON 保存、用户名读取
│   └── github_batch.py       # Day5 综合练习入口：并发批量查询
|
├── day6/                 # Day6 Git / Linux / 环境变量练习
│   └── os_test.py            # 读取环境变量练习（os.getenv）
|
├── day7/                 # Day7 pytest 基础测试
│   ├── __init__.py
│   ├── models.py             # 待测 Pydantic 模型 GitHubUser
│   ├── file_utils_demo.py    # 待测函数 save_user（JSON 保存 + 异常处理）
│   └── test_basic.py         # 第一个测试：assert 与 parametrize
|
├── tests/                # 测试代码目录
│   ├── day2_demo.py          # Day2 接口演示脚本（非 test_ 开头，pytest 不收集）
│   ├── test_models.py        # 测试 GitHubUser：合法数据 / 非法 followers
│   └── test_file_utils.py    # 用 tmp_path 测试 save_user
|
└── output/               # API 数据保存目录
    ├── Emma200605.json
    ├── github_users.json     # Day5 保存的批量用户数据
    └── kokozzzzzz.json
```

## 环境
- Python 3.13.14
- 操作系统：Windows / WSL (Ubuntu)

## 安装步骤

1.克隆项目
```bash
git clone https://github.com/yourname/project.git
cd project
```

2.创建虚拟环境
```bash
python -m venv .venv
```

3.激活虚拟环境

Windows:
```bash
.venv\Scripts\activate
```

macOS / Linux:
```bash
source .venv/bin/activate
```

4.安装依赖

```bash
pip install -r requirements.txt
```

5.导出依赖
```bush
pip freeze > requirements.txt
```



## 配置说明（Day 2 / Day 5 必需）

Day 2 和 Day 5 的代码需要访问 GitHub API，请按以下步骤配置 Token：

1. 复制根目录的 `.env_example` 模板为 `.env`：

   ```bash
   cp .env_example .env
   ```

   然后在 `.env` 中填入真实值：

   ```env
   GITHUB_TOKEN=你的GitHub个人访问令牌
   ```

2. 确认 `.gitignore` 中包含 `.env`，防止 Token 被提交至 Git；`.env_example` 只放变量名、不放真实值，可以提交。

3. 代码中会通过 `os.getenv("GITHUB_TOKEN")` 读取该配置。

> **⚠️ 安全提示**：Token 等同于密码，请勿直接写在代码中，也不要上传至 GitHub。

## 运行方式

**运行 Day 1：**

```bash
python -m day1.main
```

**运行 Day 2：**

```bash
python -m day2.main
```

**运行 Day 5：**

```bash
python -m day5.github_batch
```

**Day 5 对比实验：**

```bash
python day5/sync_request.py    # 同步请求
python day5/async_request.py   # 异步并发请求
```

**运行 Day 6（环境变量练习）：**

```bash
export MY_NAME=koko            # Windows PowerShell: $env:MY_NAME="koko"
python day6/os_test.py
```

**运行 Day 7（pytest 测试）：**

```bash
python -m pytest                          # 运行全部测试
python -m pytest -v                       # 显示每个用例的结果
python -m pytest day7/test_basic.py       # 只运行指定文件
python -m pytest -k "test_add"            # 按名称筛选用例
```

## 更新依赖

如果你新增了第三方库，请重新导出依赖清单：

```bash
pip freeze > requirements.txt
```

