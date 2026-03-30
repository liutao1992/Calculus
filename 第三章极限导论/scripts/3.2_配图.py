#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
3.2 左极限和右极限 配图脚本
"""

import numpy as np
import matplotlib.pyplot as plt

# 设置中文字体
plt.rcParams['font.sans-serif'] = ['Hiragino Sans GB', 'Arial Unicode MS', 'sans-serif']
plt.rcParams['axes.unicode_minus'] = False

# ========== 图1: 左右极限示意 ==========
fig, ax = plt.subplots(figsize=(10, 6))

# x < 3 的部分：y = x - 1
x_left = np.linspace(1, 2.99, 100)
y_left = x_left - 1

# x > 3 的部分：y = -2
x_right = np.linspace(3.01, 5, 100)
y_right = np.full_like(x_right, -2)

# 绘制
ax.plot(x_left, y_left, 'b-', linewidth=2, label=r'$f(x) = x - 1$ (当 $x < 3$)')
ax.plot(x_right, y_right, 'r-', linewidth=2, label=r'$f(x) = -2$ (当 $x > 3$)')

# 标注空心点和实心点
ax.scatter([3], [2], color='blue', s=100, zorder=5, facecolors='none', edgecolors='blue', linewidths=2)
ax.scatter([3], [-2], color='red', s=100, zorder=5)

# 标注极限值
ax.annotate(r'$\lim_{x \to 3^-} f(x) = 2$', xy=(2.85, 2), xytext=(2.2, 2.5),
            fontsize=12, color='blue',
            arrowprops=dict(arrowstyle='->', color='blue', lw=1.5))

ax.annotate(r'$\lim_{x \to 3^+} f(x) = -2$', xy=(3.15, -2), xytext=(3.8, -1.3),
            fontsize=12, color='red',
            arrowprops=dict(arrowstyle='->', color='red', lw=1.5))

# 参考线
ax.axhline(y=2, color='blue', linestyle='--', alpha=0.3)
ax.axhline(y=-2, color='red', linestyle='--', alpha=0.3)
ax.axvline(x=3, color='gray', linestyle=':', alpha=0.5)

ax.set_xlim(1, 5)
ax.set_ylim(-3, 2.5)
ax.set_xlabel(r'$x$', fontsize=14)
ax.set_ylabel(r'$f(x)$', fontsize=14)
ax.set_title(r'左右极限示例：$\lim_{x \to 3^-} f(x) \neq \lim_{x \to 3^+} f(x)$', fontsize=14)
ax.legend(loc='upper right', fontsize=11)
ax.grid(True, alpha=0.3)

plt.tight_layout()
plt.savefig('../imgs/3.2_图1_左右极限.png', dpi=150, bbox_inches='tight')
plt.close()

# ========== 图2: 极限存在与不存在对比 ==========
fig, axes = plt.subplots(1, 2, figsize=(14, 5))

# 左图：极限存在
ax1 = axes[0]
x1 = np.linspace(0, 4, 200)
y1 = x1 - 1
# 让 x=2 处的点为空心
mask = np.abs(x1 - 2) > 0.05
ax1.plot(x1[mask], y1[mask], 'b-', linewidth=2)
ax1.scatter([2], [1], color='blue', s=100, zorder=5, facecolors='none', edgecolors='blue', linewidths=2)
ax1.axvline(x=2, color='gray', linestyle=':', alpha=0.5)
ax1.annotate(r'$\lim_{x \to 2} f(x) = 1$', xy=(2, 1), xytext=(2.5, 1.5),
            fontsize=12, color='green')
ax1.set_xlim(0, 4)
ax1.set_ylim(-1, 3)
ax1.set_xlabel(r'$x$', fontsize=12)
ax1.set_ylabel(r'$f(x)$', fontsize=12)
ax1.set_title('极限存在', fontsize=13, color='green')
ax1.grid(True, alpha=0.3)
ax1.text(2, 2.7, r'$\lim_{x \to 2^-} f(x) = \lim_{x \to 2^+} f(x) = 1$',
        ha='center', fontsize=11, color='green')

# 右图：极限不存在
ax2 = axes[1]
x2_left = np.linspace(0, 2, 100)
y2_left = x2_left - 1
x2_right = np.linspace(2, 4, 100)
y2_right = x2_right + 1
ax2.plot(x2_left, y2_left, 'b-', linewidth=2)
ax2.plot(x2_right, y2_right, 'r-', linewidth=2)
ax2.axvline(x=2, color='gray', linestyle=':', alpha=0.5)

# 标注
ax2.annotate(r'$\lim_{x \to 2^-} f(x) = 1$', xy=(1.95, 1), xytext=(1.2, 1.8),
            fontsize=11, color='blue',
            arrowprops=dict(arrowstyle='->', color='blue', lw=1.5))
ax2.annotate(r'$\lim_{x \to 2^+} f(x) = 3$', xy=(2.05, 3), xytext=(2.5, 3.3),
            fontsize=11, color='red',
            arrowprops=dict(arrowstyle='->', color='red', lw=1.5))

ax2.set_xlim(0, 4)
ax2.set_ylim(-1, 4)
ax2.set_xlabel(r'$x$', fontsize=12)
ax2.set_ylabel(r'$f(x)$', fontsize=12)
ax2.set_title('极限不存在 (DNE)', fontsize=13, color='red')
ax2.grid(True, alpha=0.3)
ax2.text(2, 3.7, r'$1 \neq 3 \Rightarrow \text{DNE}$',
        ha='center', fontsize=11, color='red')

plt.suptitle('极限存在条件对比', fontsize=14, y=1.02)
plt.tight_layout()
plt.savefig('../imgs/3.2_图2_极限存在条件.png', dpi=150, bbox_inches='tight')
plt.close()

print("3.2 配图生成完成！")
