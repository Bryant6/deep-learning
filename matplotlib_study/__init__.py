# -*-coding:utf-8-*-
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-3, 3, 50)
y1 = 2 * x + 1
y2 = x ** 2
plt.figure()
plt.plot(x, y1)

plt.figure()
plt.plot(x, y2)
plt.plot(x, y1, color='red', linewidth=1.0, linestyle='--')
plt.xlim((-1, 2))
plt.ylim((-2, 3))
plt.xlabel('x zhou')
plt.ylabel('y zhou')

new_ticks = np.linspace(-1, 2, 5)
print(new_ticks)
plt.xticks(new_ticks)
plt.yticks([-2, -1.8, -1, 1.22, 3],
           [r'$really\ bad$', r'$bad\ \alpha$', 'normal', 'good', 'really good'])
# gca = get current axis
axis = plt.gca()
axis.spines['right'].set_color('none')
axis.spines['top'].set_color('none')
axis.xaxis.set_ticks_position('bottom')
axis.yaxis.set_ticks_position('left')
axis.spines['bottom'].set_position(('data', 0))
axis.spines['left'].set_position(('data', 0))

# =========================================================
# 图例
# =========================================================
plt.figure()
l1, = plt.plot(x, y2, label='up')
l2, = plt.plot(x, y1, color='red', linewidth=1.0, linestyle='--', label='down')
plt.legend(handles=[l1, l2,], labels=['line1', 'line2'], loc='best')

# =========================================================
# 注解
# =========================================================
plt.figure()
plt.plot(x, y1)

axis = plt.gca()
axis.spines['right'].set_color('none')
axis.spines['top'].set_color('none')
axis.xaxis.set_ticks_position('bottom')
axis.spines['bottom'].set_position(('data', 0))
axis.yaxis.set_ticks_position('left')
axis.spines['left'].set_position(('data', 0))

x0 = 1
y0 = 2 * x0 + 1
plt.scatter(x0, y0, s=50, color='b')
plt.plot([x0, x0], [y0, 0], 'k--', lw=2.5)

plt.annotate('2x+1=%d' % y0, xy=(x0, y0), xycoords='data', xytext=(+30, -30), textcoords='offset points',
             fontsize=16, arrowprops=dict(arrowstyle='->', connectionstyle='arc3, rad=.2'))
plt.text(-3.7, 3, r'$This\ is\ the\ some\ text.\ \mu\ \sigma_i\ \alpha_t$',
         fontdict={'size': 16, 'color': 'r'})

# =========================================================
# tick能见度
# =========================================================
x = np.linspace(-3, 3, 50)
y = 0.1*x

plt.figure()
# 在 plt 2.0.2 或更高的版本中, 设置 zorder 给 plot 在 z 轴方向排序
plt.plot(x, y, linewidth=10, zorder=1)
plt.ylim(-2, 2)
ax = plt.gca()
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
ax.spines['top'].set_color('none')
ax.xaxis.set_ticks_position('bottom')
ax.spines['bottom'].set_position(('data', 0))
ax.yaxis.set_ticks_position('left')
ax.spines['left'].set_position(('data', 0))

for label in ax.get_xticklabels() + ax.get_yticklabels():
    label.set_fontsize(12)
    # 在 plt 2.0.2 或更高的版本中, 设置 zorder 给 plot 在 z 轴方向排序
    label.set_bbox(dict(facecolor='white', edgecolor='None', alpha=0.7, zorder=2))


plt.show()
