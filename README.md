# 🕵️ GIT SPECTOR

```text
    ______ _  __     _____                     __               
   / ____/(_)/ /_   / ___/ ____  ___   _____  / /_ ____   _____ 
  / / __ / // __/   \__ \ / __ \/ _ \ / ___/ / __// __ \ / ___/ 
 / /_/ // // /_    ___/ // /_/ /  __/(__  ) / /_ / /_/ // /     
 \____//_/ \__/   /____// .___/\___//____/  \__/ \____//_/      
                       /_/                                      
```

<div align="center">

[![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![MCP](https://img.shields.io/badge/MCP-Framework-blueviolet?style=for-the-badge)](https://modelcontextprotocol.io/)
[![GitHub API](https://img.shields.io/badge/GitHub-API-black?style=for-the-badge&logo=github)](https://docs.github.com/en/rest)
[![License](https://img.shields.io/badge/License-MIT-green.svg?style=for-the-badge)](LICENSE)

**"A specialized MCP lens for your GitHub ecosystem."**
透视 GitHub 生态的专业 MCP 棱镜。

[Installation](#installation) • [Tools](#available-tools) • [Features](#features) • [Tech Stack](#tech-stack)

</div>

---

## ⚡ What is GitSpector?

**GitSpector** 是一个基于 **Model Context Protocol (MCP)** 框架构建的高级 GitHub 交互工具。它建立了一套清晰的客户端-服务器架构，让 AI 模型（如 Claude, Gemini）能够通过标准化的协议直接“读写” GitHub。

**不只是 API 封装，这是 AI 时代的 GitHub 指挥中心。**

## 🚀 Features

- **🕵️ MCP-Powered Inspection**: 利用 Anthropic 的 MCP 协议，实现工具发现与调用的标准化。
- **📂 Deep Repository Insight**: 从获取 Profile 到读取源码，提供全方位的仓库分析能力。
- **🌟 Seamless Interaction**: 一键 Star/Unstar，像本地操作一样流畅地与社区互动。
- **🚀 Scalable Architecture**: 易于扩展的服务器端逻辑，支持未来集成更多 GitHub REST/GraphQL 接口。

## 🛠️ Available Tools

GitSpector 暴露出以下核心工具供 MCP 客户端调用：

- `get_github_profile`: 探测用户画像与活跃度。
- `list_repos`: 递归获取仓库列表。
- `read_file`: 深度读取任意仓库的源文件。
- `star_repo` / `unstar_repo`: 快速社交互动。

## 📦 Installation

### 1. 克隆项目
```bash
git clone https://github.com/SaintFore/GitSpector.git
cd GitSpector
```

### 2. 环境配置
创建 `.env` 文件并填入你的 GitHub 令牌：
```env
GITHUB_TOKEN=your_github_personal_access_token
```

### 3. 启动服务器
```bash
python mcp_server.py
```

## 💻 Usage

配合支持 MCP 的客户端（如 Claude Desktop 或自定义客户端）：
```bash
python mcp_client.py
```

## 🛠️ Tech Stack

- **Framework**: Model Context Protocol (MCP)
- **Language**: Python 3.10+
- **API**: GitHub REST API
- **Environment**: Dotenv for secret management

---

<div align="center">
Created with 🕵️ by <a href="https://github.com/SaintFore">SaintFore</a>
</div>
