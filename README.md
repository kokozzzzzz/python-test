# Python 项目练习（Day 1 - Day 2）

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

## 项目结构

```text
python-test/
├── .env                  # 本地私有配置，存放 Token（不提交至 Git）
├── .gitignore
├── requirements.txt
├── README.md
├── data/                 # Day1 保存的学生数据
│   └── students.json
├── day1/                 # Day 1 独立迷你项目
│   ├── __init__.py
│   ├── main.py           # Day1 入口文件
│   └── student.py        # Student 类定义
├── day2/                 # Day 2 独立迷你项目
│   ├── __init__.py
│   ├── api_demo.py       # 接口测试调试脚本
│   ├── api.py            # 负责网络请求
│   ├── file_utils.py     # 负责数据筛选与保存
│   └── main.py           # Day2 入口文件
└── output/               # Day2 保存的 API 数据
    ├── Emma200605.json
    └── kokozzzzzz.json
```

## 环境
- Python 3.13.14
- 操作系统：Windows

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



## 配置说明（Day 2 必需）

Day 2 的代码需要访问 GitHub API，请按以下步骤配置 Token：

1. 在项目根目录创建 `.env` 文件，内容如下：

   ```env
   GITHUB_TOKEN=你的GitHub个人访问令牌
   ```

2. 确认 `.gitignore` 中包含 `.env`，防止 Token 被提交至 Git。

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

## 更新依赖

如果你新增了第三方库，请重新导出依赖清单：

```bash
pip freeze > requirements.txt
```