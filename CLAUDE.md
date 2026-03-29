# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## 项目概述

这是一个 Obsidian 个人知识库，用于存储微积分学习笔记。笔记以中文编写，采用标准的 Obsidian 目录结构组织。

## 笔记结构

```
微积分/
└── 第1 章 函数、图像和直线/
    ├── 1.1 函数.md
    └── 1.2 反函数.md
```

笔记按章节组织，每章包含多个主题的 Markdown 文件。

## 技术说明

- **笔记格式**：Markdown，支持 LaTeX 数学公式（如 $f(x)$、$\mathbb{R}$）
- **无构建系统**：纯静态 Markdown 文件，无需编译或构建
- **版本控制**：通过 Git 进行版本管理（.git 目录已配置）

## Obsidian Vault 配置

- 配置文件位于父目录的 `.obsidian/` 文件夹中
- 包含 appearance.json、core-plugins.json、workspace.json 等 Obsidian 配置

## 注意事项

- 这是一个学习笔记仓库，不是软件项目
- 无需运行测试、构建或 lint 命令
- 编辑时保持 Markdown 格式和 LaTeX 数学公式的正确性
