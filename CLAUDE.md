# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## 项目概述

这是一个 Obsidian 个人知识库，用于存储微积分学习笔记。笔记以中文编写，采用标准的 Obsidian 目录结构组织。

## 笔记结构

```
微积分/
├── 第一章函数图像和直线/
│   ├── imgs/            # 本章配图
│   ├── scripts/         # 本章脚本
│   ├── 1.1 函数.md
│   ├── 1.2 反函数.md
│   └── 1.3 直线与一次函数.md
├── 第二章三角学回顾/
│   ├── imgs/            # 本章配图
│   ├── scripts/         # 本章脚本
│   ├── 2.1 基础知识.md
│   └── 2.2 扩展三角函数定义域.md
└── 第三章极限导论/
    ├── imgs/            # 本章配图
    ├── scripts/         # 本章脚本
    ├── 3.1 极限：基本思想.md
    └── 3.2 左极限和右极限.md
```

**资源存储规则**：每个章节的配图和脚本统一存放在该章节目录下：
- 配图：存放在章节的 `imgs/` 子目录下
- 脚本：存放在章节目录下（如 `3.2_配图.py`）

笔记按章节组织，每章包含多个主题的 Markdown 文件和对应的 Python 配图脚本。

## 常用命令

### 激活虚拟环境
```bash
source /Users/liutao/Documents/Obsidian/微积分/.venv/bin/activate
```

### 运行配图生成脚本
```bash
# 方法1：在对应章节目录下，激活虚拟环境后运行
cd 第三章极限导论/scripts
source /Users/liutao/Documents/Obsidian/微积分/.venv/bin/activate
python3 3.2_配图.py

# 方法2：直接使用虚拟环境的 Python 完整路径（推荐）
cd 第三章极限导论/scripts
/Users/liutao/Documents/Obsidian/微积分/.venv/bin/python3.13 3.2_配图.py
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

## 虚拟环境使用经验

### 虚拟环境信息
- **位置**：`/Users/liutao/Documents/Obsidian/微积分/.venv`
- **Python 版本**：3.13
- **已安装包**：numpy, matplotlib

### 常见问题

**问题1：`source activate` 后 `python3` 仍用系统 Python**
- **原因**：`activate` 脚本只修改 PATH，但系统 Python 可能优先级更高
- **解决**：直接用完整路径 `/Users/liutao/Documents/Obsidian/微积分/.venv/bin/python3.13`

**问题2：脚本中用相对路径，运行时找不到**
- **原因**：相对路径基于当前工作目录，而非脚本所在位置
- **解决**：先 `cd` 到正确目录再运行脚本

**问题3：pip 安装的包 import 不到**
- **原因**：虚拟环境不完整或 PATH 混乱
- **解决**：用完整路径 `/Users/liutao/Documents/Obsidian/微积分/.venv/bin/python3.13 -m pip install xxx`

## matplotlib 配图经验

### 中文字体显示问题
**问题**：配图中使用 `family='monospace'`（等宽字体）导致中文无法显示。

**原因**：等宽字体族不包含中文字体，matplotlib 会降级到默认字体但无法渲染中文。

**教训**：
- 绘制包含中文的文本时，**禁止使用** `family='monospace'`、`family='Courier'` 等等宽字体
- 只使用 sans-serif 字体族（matplotlib 默认已配置 Hiragino Sans GB 等中文字体）
- 如果需要等宽外观用于数学公式，使用 `family='serif'` 或不指定 family

### LaTeX 分段函数标注问题
**问题**：`ax.text()` 中使用 `\begin{cases}...\end{cases}` 导致 `ParseFatalException: Unknown symbol: \begin`

**原因**：matplotlib 的文本渲染不支持 `cases` 环境

**解决**：将分段函数展开为普通文本格式，例如：
- ❌ `r'$f(x) = \begin{cases} x + 2 & x \neq 2 \\ 0 & x = 2 \end{cases}$'`
- ✅ `r'$f(x) = x + 2 \ (x \neq 2),\ f(2) = 0$'`

### 公式标注位置重叠问题
**问题**：函数表达式标注与函数曲线重叠，或同一位置出现多个相同标注（重影）

**原因1**：使用绝对坐标时，没考虑函数线位置，标注恰好落在函数线上

**原因2**：同一标注写了两次（绝对坐标 + 相对坐标各一次），导致重叠

**解决**：
- 使用 `transform=ax.transAxes` 进行相对定位（0-1 范围）
- 标注放在左上角 `ax.text(0.15, 0.92, ...)` 或右上角 `ax.text(0.85, 0.92, ...)`
- **确保每个标注只写一次**，避免重复
- 生成后检查配图是否清晰可读，必要时调整