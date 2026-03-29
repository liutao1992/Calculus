#!/usr/bin/env python3
"""
绘制上域与值域图
"""

import numpy as np
import matplotlib.pyplot as plt
import matplotlib
from matplotlib import font_manager
matplotlib.use('Agg')

font_path = '/System/Library/Fonts/STHeiti Medium.ttc'
font_prop = font_manager.FontProperties(fname=font_path)

plt.rcParams['axes.unicode_minus'] = False

fig, ax = plt.subplots(figsize=(10, 8))

x = np.linspace(-3, 3, 400)
y = x**2

ax.plot(x, y, 'b-', linewidth=2.5, label=r'$f(x) = x^2$')
ax.axhline(y=0, color='black', linewidth=0.5)
ax.axvline(x=0, color='black', linewidth=0.5)

# 上域（可能输出的集合）
ax.annotate('', xy=(4.5, 0), xytext=(4.5, 9),
            arrowprops=dict(arrowstyle='<->', color='green', lw=2.5))
ax.text(5.2, 4.5, 'Codomain\n上域\n(可能输出)', fontsize=14, color='green', va='center', fontproperties=font_prop)

# 值域（实际输出的集合）
ax.annotate('', xy=(5.2, 0), xytext=(5.2, 9),
            arrowprops=dict(arrowstyle='<->', color='orange', lw=2.5))
ax.text(5.9, 4.5, 'Range\n值域\n(实际输出)', fontsize=14, color='orange', va='center', fontproperties=font_prop)

# 填充值域区域
ax.fill_between(x, y, alpha=0.2, color='orange')

# 标注
ax.text(0, 10, r'$f(x) = x^2, \text{Domain} = \mathbb{R}$', fontsize=14, ha='center', fontproperties=font_prop)
ax.text(0, -1.5, r'$\text{Codomain} = \mathbb{R}, \text{Range} = [0, +\infty)$', fontsize=12, ha='center')

ax.set_xlim(-4, 7)
ax.set_ylim(-2, 12)
ax.set_xlabel('x', fontsize=14)
ax.set_ylabel('y', fontsize=14)
ax.set_title('上域 vs 值域', fontsize=18, fontweight='bold', fontproperties=font_prop)
ax.legend(loc='upper right', fontsize=12)
ax.grid(True, alpha=0.3)

plt.tight_layout()
plt.savefig('/Users/liutao/Documents/Obsidian/微积分/imgs/domain_range.png', dpi=150, bbox_inches='tight')
print("Saved: imgs/domain_range.png")
plt.close()
