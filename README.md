# 🕵️ GitSpector

GitSpector 是一个基于 `mcp` 框架构建的工具，它允许你通过客户端-服务器架构与 GitHub API 进行交互。

## ✨ 主要功能

GitSpector 服务器提供了一系列与 GitHub API 交互的工具，包括：

- **`hello_user`**: 一个简单的问候工具。
- **`get_github_profile`**: 获取用户的 GitHub 个人资料。
- **`list_repos`**: 列出用户的公共仓库。
- **`read_file`**: 读取仓库中文件的内容。
- **`star_repo`**: 为仓库点赞。
- **`unstar_repo`**: 取消为仓库点赞。

## 🛠️ 如何使用

### 1. 安装依赖

```bash
pip install -r requirements.txt
```

### 2. 设置 GitHub Token

为了使用 GitSpector，你需要一个 GitHub Personal Access Token。你可以在 [GitHub Developer Settings](https://github.com/settings/tokens) 中创建一个。

然后，在项目根目录下创建一个 `.env` 文件，并添加以下内容：

```
GITHUB_TOKEN=your_github_token
```

### 3. 运行服务器

```bash
python mcp_server.py
```

### 4. 运行客户端

```bash
python mcp_client.py
```

客户端将会连接到服务器，列出所有可用的工具，并调用 `star_repo` 工具。

## 🤝 贡献

欢迎任何形式的贡献！如果你有任何建议或问题，请随时提出 Issue。
