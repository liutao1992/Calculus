# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## 项目概述

这是一个 Obsidian 个人知识库，用于存储微积分学习笔记。笔记以中文编写，采用标准的 Obsidian 目录结构组织。

## 笔记结构

```
微积分/
├── 第一章函数图像和直线/
│   ├── imgs/            # 本章配图
│   ├── 1.1 函数.md
│   ├── 1.2 反函数.md
│   ├── 1.3 直线与一次函数.md
│   └── *.py             # 本章配图生成脚本
├── 第二章三角学回顾/
│   ├── imgs/            # 本章配图（如 2.2_图1_四象限.png）
│   ├── 2.1 基础知识.md
│   ├── 2.2 扩展三角函数定义域.md
│   ├── 2.1_配图.py      # 三角学配图生成脚本
│   └── 2.2_配图.py      # 扩展三角函数配图生成脚本
└── 第三章极限导论/
    ├── imgs/            # 本章配图（如 3.1_图1_函数洞.png）
    ├── 3.1 极限：基本思想.md
    └── 3.1_配图.py      # 极限配图生成脚本
```

**配图存储规则**：每个章节的配图统一存放在该章节的 `imgs/` 子目录下。

笔记按章节组织，每章包含多个主题的 Markdown 文件和对应的 Python 配图脚本。

## 常用命令

### 激活虚拟环境
```bash
source /Users/liutao/Documents/Obsidian/微积分/.venv/bin/activate
```

### 运行配图生成脚本
```bash
# 在对应章节目录下运行
python3 *.py

# 或使用虚拟环境的 Python 完整路径
/Users/liutao/Documents/Obsidian/微积分/.venv/bin/python3 *.py
```

## 技术说明

- **笔记格式**：Markdown，支持 LaTeX 数学公式（如 $f(x)$、$\mathbb{R}$）
- **配图要求**：
  - 使用 matplotlib 绘制精美的插图
  - 配图中的文字必须使用中文（字体：Hiragino Sans GB）
  - **配图存储在各章节的 `imgs/` 子目录下**（非统一目录）
- **虚拟环境**：`/Users/liutao/Documents/Obsidian/微积分/.venv`（已安装 numpy、matplotlib）
- **无构建系统**：纯静态 Markdown 文件，无需编译或构建
- **版本控制**：通过 Git 进行版本管理

## 注意事项

- 这是一个学习笔记仓库，不是软件项目
- 无需运行测试、构建或 lint 命令
- 编辑时保持 Markdown 格式和 LaTeX 数学公式的正确性
- 生成配图时优先使用虚拟环境中的 Python

## matplotlib 配图经验

### 中文字体显示问题
**问题**：配图中使用 `family='monospace'`（等宽字体）导致中文无法显示。

**原因**：等宽字体族不包含中文字体，matplotlib 会降级到默认字体但无法渲染中文。

**教训**：
- 绘制包含中文的文本时，**禁止使用** `family='monospace'`、`family='Courier'` 等等宽字体
- 只使用 sans-serif 字体族（matplotlib 默认已配置 Hiragino Sans GB 等中文字体）
- 如果需要等宽外观用于数学公式，使用 `family='serif'` 或不指定 family
